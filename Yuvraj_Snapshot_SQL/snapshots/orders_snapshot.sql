{% snapshot orders_snapshot %}
{{
  config({    
    "strategy": 'timestamp',
    "target_database": "JAFFLE_SHOP",
    "target_schema": "SNAPSHOT",
    "unique_key": "ORDER_ID",
    "updated_at": "CHANGE_DATE"
  })
}}

WITH orders_model AS (

  SELECT *
  
  FROM {{ ref('orders_model')}}

)

SELECT *

FROM orders_model

{% endsnapshot %}
