select
    round(AVG(CASE
             WHEN LENGTH IS NULL THEN 10
             ELSE LENGTH
             END), 2) AS AVERAGE_LENGTH
from FISH_INFO;