SELECT A.MEMBER_NAME, B.REVIEW_TEXT, DATE_FORMAT(B.REVIEW_DATE, '%Y-%m-%d')
FROM MEMBER_PROFILE A
JOIN REST_REVIEW B ON A.MEMBER_ID = B.MEMBER_ID
WHERE A.MEMBER_ID = (
	SELECT MEMBER_ID
	FROM REST_REVIEW
	GROUP BY MEMBER_ID
	ORDER BY COUNT(*) DESC
	LIMIT 1
)
ORDER BY B.REVIEW_DATE, B.REVIEW_TEXT;
