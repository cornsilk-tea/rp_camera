from datetime import datetime
import cv2
import time
from pathlib import Path
TIMER = int(3)
cap = cv2.VideoCapture(0)
while True:
	ret, img = cap.read()
	cv2.imshow('a', img)
	k = cv2.waitKey(125)
	if k == ord('q'):
		prev = time.time()
		while TIMER > 0:
			ret, img = cap.read()
			font = cv2.FONT_HERSHEY_SIMPLEX
			cv2.putText(img, str(TIMER),
						(200, 250), font,
						7, (0, 255, 255),
						4, cv2.LINE_AA)
			cv2.imshow('a', img)
			cv2.waitKey(125)
			cur = time.time()
			if cur-prev >= 1:
				prev = cur
				TIMER = TIMER-1
		ret, img = cap.read()
		cv2.imshow('a', img)
		now = datetime.now()
		current_time = now.strftime("%H.%M.%S")
		file_name = str(Path.joinpath(Path.cwd(), '{}.jpg'.format(current_time)))
		cv2.imwrite(file_name, img)
		print(file_name)
		TIMER = int(3)
	elif k == 27:
		break
cap.release()
cv2.destroyAllWindows()
