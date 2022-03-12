# <center> Cracking Target Confusion in End-to-end Speaker Extraction </center>

<center> Zifeng Zhao<sup>1</sup>, Dongchao Yang<sup>1</sup>, Rongzhi Gu<sup>1</sup>, Yuexian Zou<sup>1,2</sup> </center> 

<center> 1 Peking University </center>

<center> 2 Peng Cheng Laboratory</center>

## Introduction
This is a [demo](https://zhazhafon.github.io/demo-confusion/) for our paper **_Cracking Target Confusion in End-to-end Speaker Extraction_**.

## Male - Male

| speech mixture | enrollment utterance | baseline | ours | ground-truth speech | 
| :--- | :--- | :--- | :--- | :--- |
|<audio src="wavs/male2male/908-31957-0007_5105-28233-0000.wav" controls preload></audio>|<audio src="wavs/male2male/6829-68769-0023_5105-28240-0012.wav" controls preload></audio>|<audio src="wavs/male2male/baseline/908-31957-0007_5105-28233-0000.wav" controls preload></audio>|<audio src="wavs/male2male/ours/908-31957-0007_5105-28233-0000.wav" controls preload></audio>|<audio src="wavs/male2male/ours/908-31957-0007_5105-28233-0000.wav" controls preload></audio>|
|<img src="wavs/male2male/908-31957-0007_5105-28233-0000.png"/>|<img src="wavs/male2male/6829-68769-0023_5105-28240-0012.png"/>|<img src="wavs/male2male/baseline/908-31957-0007_5105-28233-0000_s1.png"/>|<img src="wavs/male2male/ours/908-31957-0007_5105-28233-0000_s1.png"/>|<img src="wavs/male2male/gt/908-31957-0007_5105-28233-0000.png"/>|
| --- | --- | --- | --- | --- |

## Model Overview
<img src="imgs/model.png" alt="Overall Architecture"/>

## Demo
### Samples from the target female singer.

| <audio src="wavs/4446-2271-0021_4970-29093-0013_mix.wav" controls preload></audio> | <audio src="wavs/4446-2271-0012_1580-141083-0012_e0.wav" controls preload></audio> | <audio src="wavs/4446-2271-0021_4970-29093-0013_est0.wav" controls preload></audio> | <audio src="wavs/4446-2271-0021_4970-29093-0013_rto0.wav" controls preload></audio> | <audio src="wavs/4446-2271-0021_4970-29093-0013_gt0.wav" controls preload></audio>
| <img src="imgs/model.png" alt="Overall Architecture"/> | <img src="imgs/model.png" alt="Overall Architecture"/> | <img src="imgs/model.png" alt="Overall Architecture"/> | <img src="imgs/model.png" alt="Overall Architecture"/> | <img src="imgs/model.png" alt="Overall Architecture"/> |

| 1 | 2 | 3 | 4 | 
| :--- | :--- | :--- | :--- |
| <audio src="wavs/ref/1.wav" controls preload></audio> | <audio src="wavs/ref/2.wav" controls preload></audio> | <audio src="wavs/ref/3.wav" controls preload></audio> | <audio src="wavs/ref/4.wav" controls preload></audio> |
| --- | --- | --- | --- |


| Source | Converted (FastSVC) | Converted (DiffSVC) |
| :--- | :--- | :--- |
| <audio src="wavs/source/0.wav" controls preload></audio> | <audio src="wavs/fastsvc/0.wav" controls preload></audio> | <audio src="wavs/diffsvc/0.wav" controls preload></audio> | 
| --- | --- | --- |
| <audio src="wavs/source/1.wav" controls preload></audio> | <audio src="wavs/fastsvc/1.wav" controls preload></audio> | <audio src="wavs/diffsvc/1.wav" controls preload></audio> | 
| --- | --- | --- |
| <audio src="wavs/source/2.wav" controls preload></audio> | <audio src="wavs/fastsvc/2.wav" controls preload></audio> | <audio src="wavs/diffsvc/2.wav" controls preload></audio> | 
| --- | --- | --- |
| <audio src="wavs/source/3.wav" controls preload></audio> | <audio src="wavs/fastsvc/3.wav" controls preload></audio> | <audio src="wavs/diffsvc/3.wav" controls preload></audio> | 
| --- | --- | --- |
| <audio src="wavs/source/4.wav" controls preload></audio> | <audio src="wavs/fastsvc/4.wav" controls preload></audio> | <audio src="wavs/diffsvc/4.wav" controls preload></audio> | 
| --- | --- | --- |
| <audio src="wavs/source/5.wav" controls preload></audio> | <audio src="wavs/fastsvc/5.wav" controls preload></audio> | <audio src="wavs/diffsvc/5.wav" controls preload></audio> | 
| --- | --- | --- |
| <audio src="wavs/source/6.wav" controls preload></audio> | <audio src="wavs/fastsvc/6.wav" controls preload></audio> | <audio src="wavs/diffsvc/6.wav" controls preload></audio> | 
| --- | --- | --- |
| <audio src="wavs/source/7.wav" controls preload></audio> | <audio src="wavs/fastsvc/7.wav" controls preload></audio> | <audio src="wavs/diffsvc/7.wav" controls preload></audio> | 
| --- | --- | --- |
| <audio src="wavs/source/8.wav" controls preload></audio> | <audio src="wavs/fastsvc/8.wav" controls preload></audio> | <audio src="wavs/diffsvc/8.wav" controls preload></audio> | 
| --- | --- | --- |
| <audio src="wavs/source/9.wav" controls preload></audio> | <audio src="wavs/fastsvc/9.wav" controls preload></audio> | <audio src="wavs/diffsvc/9.wav" controls preload></audio> | 
| --- | --- | --- |

---

### Links

[Paper] [Bibtex]

### References