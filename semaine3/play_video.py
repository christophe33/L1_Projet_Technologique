from tkinter import *
from tkinter import messagebox
import PIL.Image, PIL.ImageTk
import cv2


class Application:

    def __init__(self, window, window_title):

        self.window = window
        self.window.title(window_title)
        self.canvas = Canvas(window)
        self.canvas.pack()
        self.delay = 15   # ms
        self.open_file()
        self.play_video()
        self.window.mainloop()
        


    def open_file(self):
        self.pause = False
        self.filename = "path_video_file"
        print(self.filename)
        self.cap = cv2.VideoCapture(self.filename)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.canvas.config(width = self.width, height = self.height)


    # get only one frame    
    def get_frame(self):   
        try:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        except:
            messagebox.showerror(title='Alert', message='End of the video.')


    def play_video(self):
        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
        if not self.pause:
            self.window.after(self.delay, self.play_video)


    # Release the video source when the object is destroyed
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()


# Create a window and pass it to videoGUI Class
Application(Tk(), "Video Tracker")