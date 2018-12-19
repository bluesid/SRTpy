# SRTpy

[SRT](https://etk.srail.co.kr) wrapper for Python.

This project was inspired from [korail2](https://github.com/carpedm20/korail2) of [carpedm20](https://carpedm20.github.io).

## Requirements
- *Python3+*

## Installation

To install SRTpy, simply:

    $ pip3 install SRTpy 

Or, you can also install manually:

    $ git clone https://github.com/dotaitch/SRTpy.git
    $ cd SRTpy
    $ python3 setup.py install

## Usage

### 1. Login

First, you need to create SRT object.

```python
>>> from SRTpy import Srt, Passenger, Adult, Child, Senior, Disability1_3, Disability4_6
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

- dep : A departure station  ex) '수서', 'tntj'
- arr : A arrival station  ex) '울산', 'dnftks'
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
>>> dep = 'tntj' # 수서 
>>> arr = 'dnftks' # 울산
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

#### 2-1. About `dep` and `arr` arguments

`dep` and `arr` are the names of train stations.
*You do not need to press Kor/Eng key to write train station's name in Korean.*
If the name is in English, then convert it to Korean.

```python
>>> srt.search("tntj", "dnftks") # 수서, 울산
[[SRT 301] 12월25일 수서(05:30)->울산(07:41) 특실 예약가능 / 일반실 예약가능, 
 [SRT 305] 12월25일 수서(06:30)->울산(08:41) 특실 예약가능 / 일반실 예약가능, 
 ...,
 [SRT 331] 12월25일 수서(12:30)->울산(14:36) 특실 예약가능 / 일반실 예약가능]
 
>>> srt.search("dnftks", "ehdeorn") # 울산, 동대구
[[SRT 302] 12월25일 울산(05:23)->동대구(05:48) 특실 예약가능 / 일반실 예약가능, 
 [SRT 306] 12월25일 울산(06:23)->동대구(06:48) 특실 예약가능 / 일반실 예약가능, 
 ...,
 [SRT 336] 12월25일 울산(13:53)->동대구(14:18) 특실 예약가능 / 일반실 예약가능]
```


#### 2-2. About `passengers` argument

`passengers` is a list(or tuple) of Passenger Objects.
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

```python
>>> srt.reservations[0].cancel_time
datetime.datetime(2017, 1, 23, 5, 53, 51, 310966)
```

Reservation object has `tickets` variable.
It is a list of Ticket objects.

```python
>>> reservation.tickets
[일반실 2호차4C (어른) - 46100원,
 일반실 2호차4D (어른) - 46100원,
 일반실 2호차5C (경로) - 32300원,
 일반실 2호차5D (어린이) - 23000원]
```

# To-do

1. Cancel function

# License

Source codes are distributed under BSD license.

# Author

Heena Kwag / [@dotaitch](https://github.com/dotaitch)
