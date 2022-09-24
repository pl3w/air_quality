# Air Quality Index (AQI)

# 提供的數據
* aqi (空氣品質指標)
* pollutant (污染物)
* status 
* so2 (二氧化硫)
* co (一氧化碳)
* o3 (臭氧)
* o3_8hr (臭氧8小時平均濃度)
* pm10 (小於等於直徑10微米細懸浮微粒)
* pm2.5: pm25 (小於等於直徑2.5微米細懸浮微粒)
* no2 (二氧化氮)
* nox (氮氧化物)
* no (一氧化氮)
* wind_speed (風速)
* wind_direc (風向)
* publishtime
* co_8hr (一氧化碳8小時平均濃度)
* pm2.5_avg: pm25_avg (小於等於直徑2.5微米細懸浮微粒平均濃度)
* pm10_avg (小於等於直徑2.5微米細懸浮微粒平均濃度)
* so2_avg (二氧化硫平均濃度)


# 測站
[彰化(員林):yuanlin]()、[高雄(湖內):hunei]()、[臺南(麻豆):madou]()、[屏東(琉球):liuqiu]()、[桃園(三民):sanmin]()、[新北(樹林):shulin]()、[臺南(學甲):xuejia]()、[屏東(枋寮):fangliao]()、[基隆:keelung]()、[汐止:xizhi]()、[萬里:wanli]()、[新店:xindian]()、[土城:tucheng]()、[板橋:banqiao]()、[新莊:xinzhuang]()、[馬祖:matsu]()、[金門:kinmen]()、[馬公:magong]()、[關山:guanshan]()、[麥寮:mailiao]()、[菜寮:cailiao]()、[林口:linkou]()、[淡水:tamsui]()、[士林:shilin]()、[中山:zhongshan]()、[萬華:wanhua]()、[古亭:guting]()、[松山:songshan]()、[大同:datong]()、[桃園:taoyuan]()、[大園:dayuan]()、[觀音:guanyin]()、[平鎮:pingzhen]()、[龍潭:longtan]()、[湖口:hukou]()、[竹東:zhudong]()、[新竹:hsinchu]()、[頭份:toufen]()、[苗栗:miaoli]()、[三義:sanyi]()、[豐原:fengyuan]()、[沙鹿:shalu]()、[大里:dali]()、[忠明:zhongming]()、[西屯:xitun]()、[彰化:changhua]()、[線西:xianxi]()、[二林:erlin]()、[南投:nantou]()、[斗六:douliu]()、[崙背:lunbei]()、[新港:xingang]()、[朴子:puzi]()、[臺西:taixi]()、[嘉義:chiayi]()、[新營:sinying]()、[善化:shanhua]()、[安南:annan]()、[臺南:tainan]()、[美濃:meinong]()、[橋頭:qiaotou]()、[仁武:renwu]()、[鳳山:fengshan]()、[大寮:daliao]()、[林園:linyuan]()、[楠梓:nanzi]()、[左營:zuoying]()、[前金:qianjin]()、[小港:xiaogang]()、[屏東:pingtung]()、[潮州:chaozhou]()、[恆春:hengchun]()、[臺東:taitung]()、[花蓮:hualien]()、[陽明:yangming]()、[宜蘭:yilan]()、[冬山:dongshan]()、[三重:sanchong]()、[中壢:zhongli]()、[竹山:zhushan]()、[永和:yonghe]()、[復興:fuxing]()、[埔里:puli]()、[富貴角:fuguijiao]()、[大城:dacheng]()


# How to use
## [取得該小時數據](https://airqualityfastapi.herokuapp.com/docs#/default/get_site_special_data_api_v1__sitename___option__get)
* `https://airqualityfastapi.herokuapp.com/api/v1/{sitename}/{options}/`
```
Python 3.9.12 (main, Apr  5 2022, 01:53:17) 
[Clang 12.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> import requests
>>> res = requests.get("https://airqualityfastapi.herokuapp.com/api/v1/kinmen/pm25/")
>>> print(res.json()['data'])
[{'sitename': '金門', 'pm25': 42, 'publishtime': '2022-09-19T12:00:00'}]
>>> 

```

## [取得歷史資料](https://airqualityfastapi.herokuapp.com/docs#/default/get_site_data_with_time_interval_api_v1__sitename___option___start_time___end_time__get)
* `https://airqualityfastapi.herokuapp.com/api/v1/{sitename}/{options}/{start}/{end}/`<br>
資料始於2022-09-17 00:00:00 <br>
時間格式:`%YY%mm%dd%HH`<br>
```
Python 3.9.12 (main, Apr  5 2022, 01:53:17) 
[Clang 12.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> res = requests.get("https://airqualityfastapi.herokuapp.com/api/v1/kinmen/pm25/2022091700/2022091800")
>>> print(res.json()["data"])
[
    {
      "sitename": "金門",
      "pm25": 7,
      "publishtime": "2022-09-17T00:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 6,
      "publishtime": "2022-09-17T01:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 7,
      "publishtime": "2022-09-17T02:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 7,
      "publishtime": "2022-09-17T03:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 12,
      "publishtime": "2022-09-17T04:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 16,
      "publishtime": "2022-09-17T05:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 13,
      "publishtime": "2022-09-17T06:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 16,
      "publishtime": "2022-09-17T07:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 23,
      "publishtime": "2022-09-17T08:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 11,
      "publishtime": "2022-09-17T09:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 9,
      "publishtime": "2022-09-17T10:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 8,
      "publishtime": "2022-09-17T11:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 17,
      "publishtime": "2022-09-17T12:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 9,
      "publishtime": "2022-09-17T13:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 7,
      "publishtime": "2022-09-17T14:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 7,
      "publishtime": "2022-09-17T15:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 14,
      "publishtime": "2022-09-17T16:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 9,
      "publishtime": "2022-09-17T17:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 9,
      "publishtime": "2022-09-17T18:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 11,
      "publishtime": "2022-09-17T19:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 11,
      "publishtime": "2022-09-17T20:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 11,
      "publishtime": "2022-09-17T21:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 10,
      "publishtime": "2022-09-17T22:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 12,
      "publishtime": "2022-09-17T23:00:00"
    },
    {
      "sitename": "金門",
      "pm25": 10,
      "publishtime": "2022-09-18T00:00:00"
    }
]
>>> 

```