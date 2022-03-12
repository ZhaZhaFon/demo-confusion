# <center> Cracking Target Confusion in End-to-end Speaker Extraction </center>

<center> Zifeng Zhao<sup>1</sup>, Dongchao Yang<sup>1</sup>, Rongzhi Gu<sup>1</sup>, Yuexian Zou<sup>1,2</sup> </center> 

<center> 1 Peking University </center>

<center> 2 Peng Cheng Laboratory</center>

## Introduction
This is a [demo](https://zhazhafon.github.io/demo-confusion/) for our paper **_Cracking Target Confusion in End-to-end Speaker Extraction_**.

## Examples

### Male - Male Mixture

| <center>speech mixture</center> | <center>enrollment utterance</center> | <center>baseline</center> | <center><center>ours</center> | <center>ground-truth</center> | 
| :--- | :--- | :--- | :--- | :--- |
|<audio src="wavs/male2male/908-31957-0007_5105-28233-0000.wav" controls preload></audio>|<audio src="wavs/male2male/6829-68769-0023_5105-28240-0012.wav" controls preload></audio>|<audio src="wavs/male2male/baseline/908-31957-0007_5105-28233-0000_s1.wav" controls preload></audio>|<audio src="wavs/male2male/ours/908-31957-0007_5105-28233-0000_s1.wav" controls preload></audio>|<audio src="wavs/male2male/gt/908-31957-0007_5105-28233-0000.wav" controls preload></audio>|
|<img src="wavs/male2male/908-31957-0007_5105-28233-0000.png"/>|<img src="wavs/male2male/6829-68769-0023_5105-28240-0012.png"/>|<img src="wavs/male2male/baseline/908-31957-0007_5105-28233-0000_s1.png"/>|<img src="wavs/male2male/ours/908-31957-0007_5105-28233-0000_s1.png"/>|<img src="wavs/male2male/gt/908-31957-0007_5105-28233-0000.png"/>|
|<audio src="wavs/male2male/4077-13754-0011_2300-131720-0008.wav" controls preload></audio>|<audio src="wavs/male2male/1188-133604-0029_4077-13751-0006.wav" controls preload></audio>|<audio src="wavs/male2male/baseline/4077-13754-0011_2300-131720-0008_s0.wav" controls preload></audio>|<audio src="wavs/male2male/ours/4077-13754-0011_2300-131720-0008_s0.wav" controls preload></audio>|<audio src="wavs/male2male/gt/4077-13754-0011_2300-131720-0008.wav" controls preload></audio>|
|<img src="wavs/male2male/4077-13754-0011_2300-131720-0008.png"/>|<img src="wavs/male2male/1188-133604-0029_4077-13751-0006.png"/>|<img src="wavs/male2male/baseline/4077-13754-0011_2300-131720-0008_s0.png"/>|<img src="wavs/male2male/ours/4077-13754-0011_2300-131720-0008_s0.png"/>|<img src="wavs/male2male/gt/4077-13754-0011_2300-131720-0008.png"/>|
|<audio src="wavs/male2male/61-70968-0014_8224-274384-0003.wav" controls preload></audio>|<audio src="wavs/male2male/1221-135767-0005_61-70970-0020.wav" controls preload></audio>|<audio src="wavs/male2male/baseline/61-70968-0014_8224-274384-0003_s0.wav" controls preload></audio>|<audio src="wavs/male2male/ours/61-70968-0014_8224-274384-0003_s0.wav" controls preload></audio>|<audio src="wavs/male2male/gt/61-70968-0014_8224-274384-0003.wav" controls preload></audio>|
|<img src="wavs/male2male/61-70968-0014_8224-274384-0003.png"/>|<img src="wavs/male2male/1221-135767-0005_61-70970-0020.png"/>|<img src="wavs/male2male/baseline/61-70968-0014_8224-274384-0003_s0.png"/>|<img src="wavs/male2male/ours/61-70968-0014_8224-274384-0003_s0.png"/>|<img src="wavs/male2male/gt/61-70968-0014_8224-274384-0003.png"/>|

### Female - Female Mixture

| <center>speech mixture</center> | <center>enrollment utterance</center> | <center>baseline</center> | <center><center>ours</center> | <center>ground-truth</center> | 
| :--- | :--- | :--- | :--- | :--- |
|<audio src="wavs/female2female/8463-287645-0013_5142-33396-0037.wav" controls preload></audio>|<audio src="wavs/female2female/8463-294828-0013_1221-135767-0021.wav" controls preload></audio>|<audio src="wavs/female2female/baseline/8463-287645-0013_5142-33396-0037_s0.wav" controls preload></audio>|<audio src="wavs/female2female/ours/8463-287645-0013_5142-33396-0037_s0.wav" controls preload></audio>|<audio src="wavs/female2female/gt/8463-287645-0013_5142-33396-0037.wav" controls preload></audio>|
|<img src="wavs/female2female/8463-287645-0013_5142-33396-0037.png"/>|<img src="wavs/female2female/8463-294828-0013_1221-135767-0021.png"/>|<img src="wavs/female2female/baseline/8463-287645-0013_5142-33396-0037_s0.png"/>|<img src="wavs/female2female/ours/8463-287645-0013_5142-33396-0037_s0.png"/>|<img src="wavs/female2female/gt/8463-287645-0013_5142-33396-0037.png"/>|
|<audio src="wavs/female2female/237-134500-0002_4970-29093-0019.wav" controls preload></audio>|<audio src="wavs/female2female/4970-29095-0009_5639-40744-0014.wav" controls preload></audio>|<audio src="wavs/female2female/baseline/237-134500-0002_4970-29093-0019_s1.wav" controls preload></audio>|<audio src="wavs/female2female/ours/237-134500-0002_4970-29093-0019_s1.wav" controls preload></audio>|<audio src="wavs/female2female/gt/237-134500-0002_4970-29093-0019.wav" controls preload></audio>|
|<img src="wavs/female2female/237-134500-0002_4970-29093-0019.png"/>|<img src="wavs/female2female/4970-29095-0009_5639-40744-0014.png"/>|<img src="wavs/female2female/baseline/237-134500-0002_4970-29093-0019_s1.png"/>|<img src="wavs/female2female/ours/237-134500-0002_4970-29093-0019_s1.png"/>|<img src="wavs/female2female/gt/237-134500-0002_4970-29093-0019.png"/>|
|<audio src="wavs/female2female/4446-2275-0042_3570-5696-0004.wav" controls preload></audio>|<audio src="wavs/female2female/3570-5695-0007_5105-28233-0001.wav" controls preload></audio>|<audio src="wavs/female2female/baseline/4446-2275-0042_3570-5696-0004_s1.wav" controls preload></audio>|<audio src="wavs/female2female/ours/4446-2275-0042_3570-5696-0004_s1.wav" controls preload></audio>|<audio src="wavs/female2female/gt/4446-2275-0042_3570-5696-0004.wav" controls preload></audio>|
|<img src="wavs/female2female/4446-2275-0042_3570-5696-0004.png"/>|<img src="wavs/female2female/3570-5695-0007_5105-28233-0001.png"/>|<img src="wavs/female2female/baseline/4446-2275-0042_3570-5696-0004_s1.png"/>|<img src="wavs/female2female/ours/4446-2275-0042_3570-5696-0004_s1.png"/>|<img src="wavs/female2female/gt/4446-2275-0042_3570-5696-0004.png"/>|

## Model Overview
<img src="imgs/model.png" alt="Overall Architecture"/>

### Links

[Paper] [Bibtex]

### References