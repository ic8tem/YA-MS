[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · **中文 (繁體)**

# 流星雨

*頁籤：流星雨。*

[![流星雨](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

所有計算所用的流星雨目錄：來自 **IMO Meteor Shower Calendar 2026 與 2027**（表 5 與 7）的 **45 個流星雨**，再加上**反日點源**（表 6），每個都附有**下次峰值**。

## 欄位

| 欄位 | 意義 |
|---|---|
| 代號 | IMO 代號（QUA、PER、GEM、…） |
| 流星雨 | 名稱 |
| 活動 | 活動期間（日/月 – 日/月） |
| λ max | 峰值時的太陽黃經（J2000），取自 IMO |
| **下次峰值（UTC）** | 下次峰值的日期與時間（見下文） |
| **峰值來源** | *IMO 2026* / *IMO 2027* = IMO 公布的日期與時間；*IMO 2026（日）* = IMO 只提供日期，顯示的時間為計算值（*~hh:mm 計算值*）；*由 λ 計算* = 該年沒有 IMO 數值 |
| 赤經、赤緯 | 峰值時的輻射點（反日點源為*移動中*） |
| v km/s、r | 地心速度與族群指數 |
| ZHR | 峰值 ZHR（*多種* = 可變） |
| 類型 | *目視* 或 *無線電，白晝* |
| 今日活躍 | 流星雨目前活躍時顯示*是* |

## 下次峰值

程式一律顯示**下一次**峰值。如果 IMO 已公布當年的日曆，就使用 `data/massimi_imo.csv` 中的 **IMO 日期與時間**（已包含 2026 與 2027 年）；否則計算太陽到達峰值太陽黃經的時刻（Meeus，*Astronomical Algorithms*，第 25 章，以牛頓法求解）。

**驗證：** 在 IMO 有提供時間的情況下，計算結果與 IMO 2026 與 2027 年日曆相差在幾分鐘以內（例如象限儀座流星雨 2026 年 1 月 3 日 21:13，IMO 為 21:00；雙子座流星雨 2027 年 12 月 14 日 19:51，IMO 為 20:00）。例外：2026 年的白晝 κ-獅子座流星雨晚了一天（9 月 26 日而非 9 月 25 日），以及 2027 年 η-寶瓶座流星雨的時間（15:10，IMO 為 09:00）：這些情況下使用 IMO 的數值。

**新增年份：** IMO 公布新日曆後，將其各行加入 `data/massimi_imo.csv`（`year;code;MM-DD;hh:mm`，若 IMO 只提供日期，時間留空）。在此之前，峰值以計算得出。

## 小型與白晝流星雨

目錄包含 IMO 清單中的**小型流星雨**，例如十月鹿豹座流星雨（OCT，ZHR 5，10 月 5–6 日活躍）、仙女座流星雨、γ-小熊座流星雨，以及 4 月至 10 月的**白晝無線電流星雨**（白晝四月雙魚座流星雨、白晝白羊座流星雨、白晝 ζ-英仙座流星雨、白晝 β-金牛座流星雨、白晝 κ-獅子座流星雨、白晝六分儀座流星雨、…）。即使 ZHR 很小，它們也會計入[路徑指數](Efficiency-Calculation-zh-tw#模型)與[建議的 Hot](Sky-View-zh-tw#建議的-hot)。IMO 沒有提供白晝無線電流星雨的 ZHR：在沒有數值的情況下，程式使用工作值 5。

## 活動曲線與輻射點漂移

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max、α0、δ0 與 λ_max 取自 IMO 日曆；斜率 B（峰值前後不同）以及每日漂移 dα/dλ、dδ/dλ 是寫在 `data/sciami.csv` 中的**工作值**（IMO 的漂移表尚未輸入）。*手冊式 9 與 13。* 反日點源的位置在 IMO 表 6 的各日期之間線性內插（`data/ant_radiante.csv`；12 月 10 日至 9 月 20 日活躍，ZHR 約 4）。

## 編輯目錄

`data/sciami.csv` 是一個可以編輯的純文字檔（分隔符號 `;`）：代號、名稱、開始與結束日期（MM-DD）、λ max、赤經、赤緯、漂移、v、r、ZHR、峰值前/後的 B、類型（V 目視，R 白晝無線電）。如果某一行有誤，程式會在啟動時顯示訊息並略過該行。

資料來源：International Meteor Organization – Meteor Shower Calendar 2026 與 2027，[www.imo.net](https://www.imo.net)（表 5、6 與 7）；Philip G0ISW（無線電最大每小時數）；Rossano IZ5TEK（scattertek）。
