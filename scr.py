from browser import *
import javascript
for i in range(30):
    timer.clear_timeout(1)
    date = javascript.Date.new()
    document["outp"].text = "Сегодня {}-{:02}-{:02} \n И время: {:02}:{:02}:{:02}".format(
        date.getFullYear(), date.getMonth()+1, date.getDate(),
        date.getHours(), date.getMinutes(), date.getSeconds())
