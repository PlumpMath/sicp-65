(defun squartRoot ( guess number)
  (if (good_enought guess number)
      guess
      (squartRoot ( nextGuess guess number) number)))

(defun good_enought( guess number)
  (< (abs (- (* guess guess) number)) 0.0001))

(defun nextGuess (guess number)
  (/ (+ guess (/ number guess)) 2))


(progn
  (format t "please enter the number: ")
  (set 'number (read)))


(float (squartRoot 1 number))