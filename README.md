# robosys

## ライセンス情報
This repository is licensed under the GPLv3 license, see LICENSE.

## 動作に必要なパッケージ
wiringpiを用いてGPIOを操作しているため
<br>本プログラム実行時には下記のコマンドなどを用いてあらかじめインストールしておく.<br>
   ```
    $ pip install wiringpi
   ```

## ファイル配置
提供されたScriptsファイルの中にある拡張子が.pyである実行ファイルを<br>
自身の環境で作成した, ROSのScriptファイルの中に配置してください.

## 課題2概要
本プログラムはGPLのもと、アップロードされている.
<br>本プログラムはROSを用いてLEDを光らすものである
<br>Publisher側では入力を受け付け, Subscriber側では入力された値をもとに出力先のPIN番号を確認することができる.

## 操作方法
  1. 起動<br>
  ```
    $ roscore  
    $ rosrun [pkg_name] led_flash_pub.py  
    $ rosrun [pkg_name] led_flash_sub.py
  ```
  
  2. 入力<br>
  ```
    $ input: [0, 1, 2, 3, 4, exit]
  ```
  
  3. 出力<br>
  ```
    例) $ 14 pin select 
  ```
  
## 動画URL(GoogleDrive Twitter)
https://drive.google.com/file/d/1MzeVCcGbIE8eBlQ-GHcbpvl2ZOpzAF7-/view?usp=sharing
https://twitter.com/karaage5daisuki/status/1205050814277943296
