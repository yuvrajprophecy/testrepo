WITH test_orders AS (

  SELECT * 
  
  FROM {{ ref('test_orders')}}

)

SELECT *

FROM test_orders
