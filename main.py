import tkinter as tk
import random
import cv2


window_height = 300
window_width = 400


canvas = tk.Tk()
canvas.geometry("400x300")
canvas.title("Dice Simulator")
canvas.iconbitmap('images/icon.ico')
canvas.configure(bg='white')
canvas.resizable(False, False)
screen_width = canvas.winfo_screenwidth()
screen_height = canvas.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
canvas.geometry("{}x{}+{}+{}".format(window_width,
                                     window_height, x_coordinate, y_coordinate))


def dice_generate():
    generated_number = random.randint(1, 6)

    if(generated_number == 1):
        image = cv2.imread("./images/one.png")
        cv2.imshow('Dice Result', image)
        cv2.waitKey(1500)
        cv2.destroyAllWindows()

    elif(generated_number == 2):
        image = cv2.imread("./images/two.png")
        cv2.imshow('Dice Result', image)
        cv2.waitKey(1500)
        cv2.destroyAllWindows()

    elif(generated_number == 3):
        image = cv2.imread("./images/three.png")
        cv2.imshow('Dice Result', image)
        cv2.waitKey(1500)
        cv2.destroyAllWindows()

    elif(generated_number == 4):
        image = cv2.imread("./images/four.png")
        cv2.imshow('Dice Result', image)
        cv2.waitKey(1500)
        cv2.destroyAllWindows()

    elif(generated_number == 5):
        image = cv2.imread("./images/five.png")
        cv2.imshow('Dice Result', image)
        cv2.waitKey(1500)
        cv2.destroyAllWindows()

    elif(generated_number == 6):
        image = cv2.imread("./images/six.png")
        cv2.imshow('Dice Result', image)
        cv2.waitKey(1500)
        cv2.destroyAllWindows()


browse_button = tk.Button(canvas, text="Roll Dice",
                          command=dice_generate, font=("SAN_SERIF", 15, "bold")).pack(pady=100)


canvas.mainloop()
