🧠 AI-Powered Shopify Analytics App
Overview
This project is a mini AI-powered analytics platform that allows Shopify merchants to ask natural-language questions about their business.
The system translates user questions into ShopifyQL, fetches data from Shopify, and explains results in simple business language.
🎯 Key Capabilities
Shopify OAuth authentication
Natural-language analytics (sales, inventory, customers)
LLM-powered ShopifyQL generation
Agentic workflow (plan → execute → explain)
Rails API gateway + Python AI service
🏗 Architecture
User / Postman
     |
     v
Rails API (Gateway)
 - OAuth
 - Validation
 - Token Security
     |
     v
Python AI Service (Agent)
 - Intent detection
 - ShopifyQL generation
 - Query execution
 - Explanation
     |
     v
Shopify Admin API + ShopifyQL
🔧 Tech Stack
| Layer         | Tech                     |
| ------------- | ------------------------ |
| API Gateway   | Ruby on Rails (API-only) |
| AI Service    | Python + FastAPI         |
| LLM           | OpenAI / Mock            |
| Analytics     | ShopifyQL                |
| Auth          | Shopify OAuth            |
| DB (Optional) | PostgreSQL               |
🚀 Setup Instructions
Rails API
cd rails-api
bundle install
rails db:create db:migrate
rails s
Python AI Service
cd python-ai-service
pip install -r requirements.txt
uvicorn main:app --reload
🔍 Sample API Request
POST /api/v1/questions
{
  "store_id": "example-store.myshopify.com",
  "question": "How much inventory should I reorder next week?"
}
Sample Response
{
  "answer": "You sell around 10 units per day. Reorder at least 70 units to avoid stockouts next week.",
  "confidence": "medium"
}
🤖 Agent Workflow
Understand intent
Decide required Shopify data
Generate ShopifyQL
Validate & execute query
Convert metrics into insights
