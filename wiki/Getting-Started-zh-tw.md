[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · **中文 (繁體)**

# 入門

首次啟動時，YA-MS 會顯示一條範例路徑（JN70CN → JO62QM，144 MHz）。只需五分鐘即可為您的電台完成設定。

## 1. 三列控制項

分頁上方有三列控制項，對所有分頁都有效。右上角的**控制**按鈕可收合和展開它們（使用大字型時很有用）；該選擇會被記住。

**第 1 列 – 電台與頻段**

| 控制項 | 作用 |
|---|---|
| **我的網格座標** / **高度 m** | 您的 Maidenhead 網格座標（4、6 或 8 位；取方格中心）以及電台的海拔高度。 |
| **對方電台** / **高度 m** | 您想通聯的電台的網格座標和高度。 |
| **頻段 MHz** | 28、50、70、144、222 或 432 MHz：用於天線增益和波瓣、流量估算以及鏈路預算。 |
| **計算** | 重新計算路徑（E 層取樣：需要幾秒鐘）。 |
| **天線方位** | 您的天線方位：始終**朝向 DX**（即路徑方位）。 |
| **字型** | 所有文字的大小，100–300 %。請參閱[設定](Settings-and-Data-Folder-zh-tw#字型與控制)。 |

**第 2 列 – E 層與天線**

| 控制項 | 作用 |
|---|---|
| **餘跡高度 km** + **來自雷達** | 流星餘跡的高度（預設 90 km）。勾選*來自雷達*時，使用 Collm 雷達測得的最常見高度（眾數）；請參閱[雷達流量](Radar-Flux-zh-tw)。 |
| **波瓣仰角 °** | 天線垂直波瓣最大值的仰角：固定在 0° 的定向天線由於地面反射，波瓣仍位於地平線以上幾度（通常 3-8°）。開啟 **天線場型** 核取方塊時（預設），E 層的點依兩副天線的垂直場型加權；關閉時只使用兩個電台都能在此仰角以上看到的點。 |
| **八木天線：橫桿 m** | 您的八木天線橫桿長度。程式顯示以 λ 表示的長度、增益（DL6WU 曲線）以及水平和垂直方向的 −3 dB 波瓣；請參閱[幾何與路徑損耗](Geometry-and-Path-Loss-zh-tw#天線增益與波瓣)。低於 2 λ 時估算較粗略。 |
| **熱點距中點 km** + **auto (AMS)** | Hot A 和 Hot B 到中點的距離。勾選 *auto (AMS)*（預設）時，依 DJ5HG 引用的 J. Richardson（AMS）天線偏角表確定：1000 km 為 13°，1250 km 為 11°，1500 和 2000 km 為 10°（距中點約 115、121、132 和 176 km）。取消勾選可手動輸入 30–400 km（MSHV 使用 150 km）。 |

**第 3 列 – 時間**

| 控制項 | 作用 |
|---|---|
| **時間** | UTC 時鐘。 |
| **計算日期（UTC）** | [預報計算](Sky-View-zh-tw)和 [GRAVES 雷達](GRAVES-Radar-zh-tw)的計算日期（預設為今天），時刻取當天的目前時間。 同時也是：[效率計算](Efficiency-Calculation-zh-tw)和 GRAVES 時間線中顯示的日期。 |
| **小時（−12 至 +36 h）** | 將計算時刻在該時間之前 12 小時到之後 36 小時之間移動，步長 15 分鐘。旁邊顯示*計算時間：目前*或*計算時間：dd/mm hh:mm UTC*。 |
| **即時** | 回到目前時刻。 |

## 2. 本台與對方電台

1. 輸入**我的網格座標**和**高度 m**。
2. 輸入**對方電台**的網格座標和高度——或在[天穹](Sky-View-zh-tw)中點選地圖：**左鍵 = 對方電台網格座標**，**右鍵 = 本台網格座標**。
3. 選擇**頻段 MHz** 並點選**計算**。

底部狀態列會確認：*路徑已計算：… km，… s 內取樣了 … 個反射點*。

## 3. 您的天線

輸入八木天線的**橫桿長度**。程式據此推算增益和波瓣；當天線指向 DX 時，如果 Hot A 或 Hot B 已經落在**波瓣內**，程式會提醒您（此時它們以灰色繪出：無需轉動天線）。

## 4. 閱讀結果

| 問題 | 查看位置 |
|---|---|
| 現在哪個流星雨對我的路徑有幫助？來自哪一側？ | [天穹](Sky-View-zh-tw)：流星雨清單、紅色的建議 Hot、PREV 區域 |
| 今天哪個時段最好？ | [效率計算](Efficiency-Calculation-zh-tw)：概覽卡片和逐時表格 |
| 雷達正在統計多少流星？ | [雷達流量](Radar-Flux-zh-tw) |
| 在 144 MHz 上我能期望多少個 ping？ | [試驗性預報](Experimental-Forecasts-zh-tw)（試驗性） |
| 我的電台能打通這條路徑嗎？ | [幾何與路徑損耗](Geometry-and-Path-Loss-zh-tw)：路徑損耗和餘裕 |
| 下一個峰值是什麼時候？ | [流星雨](Showers-zh-tw) |
| 我能用 GRAVES 做測試嗎？ | [GRAVES 雷達](GRAVES-Radar-zh-tw) |

## 實用規則（來自文獻）

- **與流星雨方向垂直指向**：最佳路徑與輻射點方位正交；最佳指向 = 輻射點方位 ±90°，容差 ±40–50°（SM6FHZ）。
- **側向散射**：將天線向大多數反射到達的一側（A 或 B）偏轉 10–30°（Cerrotta–Sartori 文章）。
- **輻射點過高**（高於 70°）或過低（低於 20°）時，有用的餘跡很少（DF5HC、DH9GCD）。
- 偶發流星在 **06 UTC** 左右達到峰值（文章；Collm 流量也證實了這一點）。
- 432 MHz 上的有效距離：800–2000 km，最佳約 1400 km（SM6FHZ）；一般而言最佳距離為 1300–1500 km（DF5HC）。

下一步：[天穹](Sky-View-zh-tw)。
