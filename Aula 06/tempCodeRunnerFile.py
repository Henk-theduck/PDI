pts1 = [[50,50],[200,50],[50,200]]
pts2 = [[10,100],[200,50],[100,250]]
M = cv2.getAffineTransform(np.float32(pts1),np.float32(pts2))