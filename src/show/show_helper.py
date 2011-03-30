from app import App

if __name__ == "__main__":
    a = App()
    a.configure_traits()
    a.ls_timer.cancel()
