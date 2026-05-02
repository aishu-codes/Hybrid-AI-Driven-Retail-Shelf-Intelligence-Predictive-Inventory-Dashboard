import winsound  # For Windows
import os
import platform

class AudioAlerts:
    def __init__(self):
        system = platform.system()
        if system == 'Windows':
            self.beep = self.windows_beep
        elif system == 'Darwin':  # macOS
            self.beep = self.mac_beep
        else:
            self.beep = self.linux_beep

    def windows_beep(self, frequency, duration):
        winsound.Beep(frequency, duration)

    def mac_beep(self, frequency=1000, duration=500):
        # Use osascript to call the system beep
        os.system(f'osascript -e "beep"')

    def linux_beep(self, frequency=1000, duration=500):
        print('\a')  # This may work in terminal that recognizes the ASCII Bell

    def low_stock_alert(self):
        self.beep(750, 1000)  # Beep for low stock

    def critical_stock_alert(self):
        self.beep(1000, 2000)  # Beep for critical stock

    def stock_restored_alert(self):
        self.beep(500, 500)  # Beep for stock restored


# Example usage:
if __name__ == '__main__':
    alerts = AudioAlerts()
    alerts.low_stock_alert()
    alerts.critical_stock_alert()
    alerts.stock_restored_alert()
