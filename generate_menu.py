import os
from datetime import datetime
from google import genai

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("找不到 GEMINI_API_KEY 環境變數！")

# 使用官方最新 SDK 初始化 Client
client = genai.Client(api_key=api_key)

today_str = datetime.now().strftime("%Y/%m/%d")

prompt = f"""
你是「公司餐點分析網」，請使用「日系明亮元氣食通信」模板，將今日（{today_str}）午餐清單製作成完整的單一 HTML 網頁。

【格式與內容規範】：
1. 輸出必須是完整的單一 HTML 代碼，風格必須是「日系明亮元氣食通信」（明亮米白底色 #fffdfa、暖陽橙橘漸層橫幅、活潑手繪雜誌感卡片）。
2. 頂部儀表板必須包含：
   - 活力標題與「今天也要好好吃飯！」元氣副標。
   - 4 個數據指標看板（總餐點數、最高評分、平均熱量、肉品數）。
   - 執事今日暖心備忘錄（幽默調侃與開會提神提醒）。
3. 包含今日餐點卡片：
   - 左側放實拍照片縮圖（請使用 Google Drive 直顯 thumbnail 格式，例如 https://drive.google.com/thumbnail?id=1GVN7-sKNz6DsQppaIJNktHAdtMl5TpAc&sz=w400）。
   - 附帶排名徽章、檔口與價格、推薦評分。
   - 4 大活力參數晶片（肉品標籤、估算熱量 kcal、蛋白質 g、飽足感等級）。
   - 底部條帶加入「執事涼話小劇場」毒舌幽默開釋。
4. 頁尾必須包含「開啟雲端實拍相簿」按鈕，並於最下方嚴格加上此版權宣告字樣：
   "Designed & Provided by PB Studio · Bear Chang © 2026 PB Studio · Bear Chang. All Rights Reserved. 僅供個人／授權範圍內使用，禁止未經同意轉載、公開散布或商業使用。"

【輸出限制】：
請直接輸出純 HTML 程式碼，絕對不要在頭尾包裹 ```html 或 ``` 等任何 markdown 標籤。
"""

# 使用最新穩定版 gemini-2.5-flash
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

html_content = response.text.replace("```html", "").replace("```", "").strip()

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[{datetime.now()}] index.html 成功生成並寫入！")
