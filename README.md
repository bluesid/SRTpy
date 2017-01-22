# SRTpy

[SRT](https://etk.srail.co.kr) wrapper for Python.

This project was inspired from [korail2](https://github.com/carpedm20/korail2) of [carpedm20](https://carpedm20.github.io).

## Installing

To install SRTpy, simply:

    $ pip install srtpy

Or, you can also install manually:

    $ git clone https://github.com/dotaitch/SRTpy.git
    $ cd SRTpy
    $ python setup.py install

## Usage

### 1. Login

First, you need to create SRT object.

```python
>>> from srt import *
>>> srt = Srt("12345678", YOUR_PASSWORD) # with membership number
>>> srt = Srt("dotaitch@gmail.com", YOUR_PASSWORD) # with email
>>> srt = Srt("010-xxxx-yyyy", YOUR_PASSWORD) # with phone number
```

If you do not want login automatically, 

```python
>>> srt = Srt("12345678", YOUR_PASSWORD, auto_login=False)
>>> srt.login()
True
```

### 2. Search trains

You can search train schedules `search` and `search_allday` methods.
`search` and `search_allday` return a list of Train objects.

- `search` returns 10 results max.
- `search_allday` returns all results after the time.
- `search_allday` uses `search` repeatedly.

`search` and `search_allday` methods take these arguments:

- dep_stn_name : A departure station in Korean  ex) '수서'
- arr_stn_name : A arrival station in Korean  ex) '울산'
- (optional) date : A departure date in `yyyyMMdd` format  ex) '20170131'
- (optional) time : A departure time in `hhmmss` format  ex) '133000'
- (optional) passengers : List of Passenger Objects. None means 1 Adult. 
- (optional) seat_option : Seat options in Korean. Default value is '일반'.
    - '일반'
    - '휠체어'
    - '전동휠체어'
- (optional) train_type : A type of train. Default value is 'SRT'.
    - '전체', 'ALL'
    - 'SRT'
    - 'SRT+KTX'
- (optional) include_no_seat : When it is True, a result includes trains which has no seats.

Below is a sample usage of `search`:

```python
>>> dep = '수서'
>>> arr = '울산'
>>> date = '20170131'
>>> time = '133000'
>>> trains = srt.search(dep, arr, date, time)
[[SRT 337] 01월31일 수서(13:30)->울산(15:37) 특실 예약가능 / 일반실 예약가능,
 [SRT 341] 01월31일 수서(14:30)->울산(16:26) 특실 예약가능 / 일반실 예약가능,
 [SRT 343] 01월31일 수서(15:00)->울산(17:10) 특실 예약가능 / 일반실 예약가능,
 [SRT 347] 01월31일 수서(16:00)->울산(18:01) 특실 예약가능 / 일반실 예약가능]
```

When you want to see sold-out trains and others.

```python
>>> trains = srt.search('동대구', '울산', date, time, train_type='전체', include_no_seat=True)
[[KTX 127] 01월31일 동대구(13:49)->울산(14:18) 특실 예약가능 / 일반실 예약가능,
 [SRT 331] 01월31일 동대구(14:12)->울산(14:36) 특실 예약가능 / 일반실 예약가능,
 [KTX 129] 01월31일 동대구(14:19)->울산(14:43) 특실 예약가능 / 일반실 예약가능,
 [SRT 337] 01월31일 동대구(15:14)->울산(15:37) 특실 예약가능 / 일반실 예약가능,
 [KTX 135] 01월31일 동대구(15:19)->울산(15:47) 특실 예약가능 / 일반실 예약가능,
 [SRT 341] 01월31일 동대구(16:02)->울산(16:26) 특실 예약가능 / 일반실 예약가능,
 [KTX-산천 139] 01월31일 동대구(16:14)->울산(16:43) 특실 예약가능 / 일반실 예약가능]
```

#### 2-1. About `passengers` argument

`passengers` is a list(or tuple) of Passeger Objects.
By this, you can search for multiple passengers.
There are 5 types of Passengers: Adult, Child, Senior, Disability1_3, and Disability4_6.

```python
# for 1 adult, 1 child
>>> psgrs = [Adult(), Child()]

# for 2 adults, 1 child
>>> psgrs = [Adult(2), Child(1)]
# ditto. They are being added each other by same group.
>>> psgrs = [Adult(), Adult(), Child()]

# for 2 adults, 1 child, 1 senior
>>> psgrs = [Adult(2), Child(), Senior()]

# for 1 adult, It supports negative count or zero count. 
# But it uses passengers which the sum is greater than zero.
>>> psgrs = [Adult(2), Adult(-1)]
>>> psgrs = [Adult(), Senior(0)]

# Nothing
>>> psgrs = [Adult(0), Senior(0)]

# then search or reserve train
>>> trains = srt.search(dep, arr, date, time, passengers=psgrs)
...
>>> srt.reserve(trains[0], passengers=psgrs)
...
```

### 3. Make a reservation

You can reserve trains with `reserve` method.
`reserve` returns Reservation object.

`reserve` methods take these arguments:

- train : Train object that you want to reserve.
- (optional) passengers : List of Passenger Objects. None means 1 Adult. 
- (optional) seat_option : Seat options in Korean. Default value is '일반'.
    - '일반'
    - '휠체어'
    - '전동휠체어'
- (optional) seat_location : Seat locations in Korean. Default value is '기본'.
    - '기본'
    - '1인석(특실)'
    - '창측'
    - '내측'
- (optional) general_seat : When it is True, you can reserve a general seat. When it is False, you can reserve a special seat.

Below is a sample usage of `reserve`:

```python
>>> trains = srt.search(dep, arr, date, time)
>>> reservation = srt.reserve(trains[0])
>>> reservation
[SRT 337] 01월31일 수서(13:30)->울산(15:37) 1매 - 46100원
```

Multiple.

```python
>>> reservation = srt.reserve(trains[0], passengers=psgrs)
>>> reservation
[SRT 340] 01월31일 수서(13:30)->울산(15:37) 4매 - 147500원
```

You can select the seat grade, general(True) or special(False) by general_seat argument.

```python
>>> srt.reserve(trains[0], passengers=psgrs, general_seat=True)
```

### 4. Show reservations ####

You can show your reservations by `reservations` variable.
It is a list of Reservation objects.

```python
>>> srt.reservations
[[SRT 337] 01월31일 수서(13:30)->울산(15:37) 1매 - 46100원,
 [SRT 340] 01월31일 수서(13:30)->울산(15:37) 4매 - 147500원]
```

You can see when the reservation is cancelled. 

```
>>> srt.reservations[0].cancel_time
datetime.datetime(2017, 1, 23, 5, 53, 51, 310966)
```

Reservation object has `tickets` variable.
It is a list of Ticket objects.

```
>>> reservation.tickets
[일반실 2호차4C (어른) - 46100원,
 일반실 2호차4D (어른) - 46100원,
 일반실 2호차5C (경로) - 32300원,
 일반실 2호차5D (어린이) - 23000원]
```

# To-do

0. Support python2
1. Cancel function
2. Constants in English

# License

Source codes are distributed under BSD license.

# Author

Heena Kwag / [@dotaitch](https://github.com/dotaitch)
