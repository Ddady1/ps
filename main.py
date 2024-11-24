import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window(size=(500, 500))

gauge = ttk.Floodgauge(
    bootstyle=INFO,
    font=(None, 24, 'bold'),
    mask='Memory Used {}%',
)
gauge.pack(fill=BOTH, expand=YES, padx=10, pady=10)

# autoincrement the gauge
gauge.start()

# stop the autoincrement
gauge.stop()

# manually update the gauge value
gauge.configure(value=0)

# increment the value by 10 steps
for i in range(100):
    gauge.step(i)
    i +=5

app.mainloop()
