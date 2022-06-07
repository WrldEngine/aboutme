from browser import *
import javascript

def time(event):
    date = javascript.Date.new()
    document["outp"].text = "Сегодня {}-{:02}-{:02} \n И время: {:02}:{:02}:{:02}".format(
        date.getFullYear(), date.getMonth()+1, date.getDate(),
        date.getHours(), date.getMinutes(), date.getSeconds())

document["btn"].bind("click", time)
