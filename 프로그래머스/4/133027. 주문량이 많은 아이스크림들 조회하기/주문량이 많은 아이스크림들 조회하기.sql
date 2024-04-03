select j.FLAVOR
FROM FIRST_HALF f
join JULY j
on f.FLAVOR = j.FLAVOR

group by f.FLAVOR
order by (SUM(j.TOTAL_ORDER) + SUM(f.TOTAL_ORDER)) desc
limit 3;