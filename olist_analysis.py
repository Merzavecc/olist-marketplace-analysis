import sqlite3
import pandas as pd

# Подключаемся к базе, которую создал load_olist.py
conn = sqlite3.connect("olist.db")

# Вопрос 1: выручка по месяцам (только полные месяцы)
q1 = """
SELECT
    strftime('%Y-%m', o.order_purchase_timestamp) AS month,
    ROUND(SUM(i.price), 0) AS revenue
FROM olist_orders_dataset o
JOIN olist_order_items_dataset i ON o.order_id = i.order_id
GROUP BY month
HAVING month BETWEEN '2017-01' AND '2018-08'
ORDER BY month
"""

# Вопрос 2: топ-10 категорий товаров по выручке
q2 = """
SELECT
    t.product_category_name_english AS category,
    ROUND(SUM(i.price), 0) AS revenue
FROM olist_order_items_dataset i
JOIN olist_products_dataset p ON i.product_id = p.product_id
JOIN product_category_name_translation t ON p.product_category_name = t.product_category_name
GROUP BY category
ORDER BY revenue DESC
LIMIT 10
"""

# Вопрос 3: топ-10 штатов по количеству заказов
q3 = """
SELECT
    c.customer_state AS state,
    COUNT(*) AS orders
FROM olist_orders_dataset o
JOIN olist_customers_dataset c ON o.customer_id = c.customer_id
GROUP BY state
ORDER BY orders DESC
LIMIT 10
"""

print("=== 1. Выручка по месяцам ===")
print(pd.read_sql(q1, conn))

print("\n=== 2. Топ-10 категорий по выручке ===")
print(pd.read_sql(q2, conn))

print("\n=== 3. Топ-10 штатов по заказам ===")
print(pd.read_sql(q3, conn))

conn.close()
