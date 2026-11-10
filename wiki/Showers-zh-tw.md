[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [ไทย](Showers-th) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · **中文 (繁體)**

# 流星雨

*分頁：流星雨。*

[![流星雨](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

所有計算所用的流星雨目錄：來自 **IMO Meteor Shower Calendar 2026 和 2027**（表 5 和 7）的 **45 個流星雨**，外加**反日點源**（表 6），每個都附有其**下一個峰值**。

## 欄位

| 欄位 | 含義 |
|---|---|
| 代碼 | IMO 代碼（QUA、PER、GEM …） |
| 流星雨 | 名稱 |
| 活動 | 活動期（日/月 – 日/月） |
| λ max | 峰值時的太陽黃經（J2000），取自 IMO |
| **下一個峰值（UTC）** | 下一個峰值的日期和時間（見下文） |
| **峰值來源** | *IMO 2026* / *IMO 2027* = IMO 公布的日期和時間；*IMO 2026（日）* = IMO 只列出日期，顯示的時間為計算值（*計算值 ~hh:mm*）；*由 λ 計算* = 該年份沒有 IMO 數值 |
| 赤經、赤緯 | 峰值時的輻射點（反日點源為*移動*） |
| v km/s、r | 地心速度和族群指數 |
| ZHR | 峰值 ZHR（*變化* = 可變） |
| 類型 | *目視* 或 *無線電，白晝* |

**今日（UTC）活躍**的流星雨以黃色半透明底色和粗體突顯。

## 下一個峰值

程式始終顯示**下一個**峰值。如果 IMO 已發布當年的日曆，就使用 `data/massimi_imo.csv` 中的 **IMO 日期和時間**（已包含 2026 和 2027 年）；否則計算太陽到達峰值太陽黃經的時刻（Meeus，*Astronomical Algorithms*，第 25 章，用牛頓法求解）。

**驗證：** 在 IMO 列出時間的情況下，計算結果與 IMO 2026 和 2027 年日曆的差異在幾分鐘以內（例如象限儀座流星雨 2026 年 1 月 3 日 21:13，IMO 為 21:00；雙子座流星雨 2027 年 12 月 14 日 19:51，IMO 為 20:00）。例外：2026 年白晝獅子座κ流星雨晚一天（9 月 26 日而非 9 月 25 日），以及 2027 年寶瓶座η流星雨的時間（15:10，IMO 為 09:00）——這些情況下使用 IMO 的數值。

**新增年份：** IMO 發布新日曆後，將其各行新增到 `data/massimi_imo.csv` 中（`year;code;MM-DD;hh:mm`，如果 IMO 只列出日期，時間留空）。在此之前，峰值由計算得出。

## 小型與白晝流星雨

目錄包含 IMO 清單中的**小型流星雨**——例如十月鹿豹座流星雨（OCT，ZHR 5，10 月 5–6 日活躍）、仙女座流星雨、小熊座γ流星雨——以及 4 月至 10 月的**白晝無線電流星雨**（白晝四月雙魚座流星雨、白晝白羊座流星雨、白晝英仙座ζ流星雨、白晝金牛座β流星雨、白晝獅子座κ流星雨、白晝六分儀座流星雨 …）。即使 ZHR 很小，它們也會計入[路徑指數](Efficiency-Calculation-zh-tw#模型)和[建議的 Hot](Sky-View-zh-tw#建議的-hot)。IMO 不提供白晝無線電流星雨的 ZHR：在沒有提供數值的情況下，程式使用工作值 5。

## 活動曲線與輻射點漂移

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

ZHR_max、α0、δ0 和 λ_max 取自 IMO 日曆；斜率 B（峰值前後不同）以及每日漂移 dα/dλ、dδ/dλ 是寫在 `data/sciami.csv` 中的**工作值**（IMO 的漂移表尚未輸入）。*手冊公式 9 和 13。* 反日點源的位置在 IMO 表 6 的各日期之間線性內插（`data/ant_radiante.csv`；12 月 10 日至 9 月 20 日活躍，ZHR 約 4）。

## 編輯目錄

`data/sciami.csv` 是一個可以編輯的純文字檔（分隔符號 `;`）：代碼、名稱、開始和結束日期（MM-DD）、λ max、赤經、赤緯、漂移、v、r、ZHR、峰值前/後的 B、類型（V 目視，R 白晝無線電）。如果某一行有誤，程式會在啟動時顯示訊息並忽略該行。

來源：International Meteor Organization – Meteor Shower Calendar 2026 和 2027，[www.imo.net](https://www.imo.net)（表 5、6 和 7）；Rossano IZ5TEK（scattertek）。
