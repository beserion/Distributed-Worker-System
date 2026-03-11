# **Beserion Distributed Worker System**

A fault-tolerant, distributed job processing system designed for high-load background task execution.
It provides master → queue → worker architecture with retry logic, visibility timeouts, monitoring, and multi-language worker support (Python + C).

This project is built to demonstrate real distributed-systems engineering and production-grade architecture.

---

## 🚀 **Features**

* **Distributed Worker System**
  Multiple workers can run on different machines and process tasks concurrently.

* **Fault-Tolerant Reaper Engine**
  Recovers stuck jobs, requeues failed tasks, and handles crash situations safely.

* **Automatic Retries & Backoff**
  Configurable retry counts, exponential backoff, and job state tracking.

* **Visibility Timeout**
  Ensures tasks are returned to the queue if a worker dies mid-process.

* **C Worker Plugin Support**
  Fast, low-level worker implemented in C to demonstrate dual-language orchestration.

* **Docker & Compose Setup**
  Easy deployment with RabbitMQ + workers + master containers.

* **Job Queue Architecture**
  Clean separation between job producers and job consumers.

* **Extensible Job Handlers**
  Add new job types easily via Python modules.

---

## 🏗️ **Architecture Overview**

```
            +------------------+
            |      Master      |
            |  job producer    |
            +--------+---------+
                     |
                     |  publish job
                     v
             +---------------+
             |   RabbitMQ    |
             | task queues   |
             +--+--------+---+
                |        |
    consume --> |        | <-- consume
                v        v
         +-----------+  +-----------+
         |  Worker1  |  |  Worker2  |
         | (Python)  |  |   (C)     |
         +-----------+  +-----------+
                |
                v
          job result/logs
                |
                v
         +-------------+
         |   Reaper    |
         | retry & fix |
         +-------------+
```

---

## 📦 **Installation**

### **1. Clone the Repository**

```bash
git clone https://github.com/beserion/Distributed-Worker-System.git
```

---

## 🐳 **Running with Docker (Recommended)**

This starts:

* RabbitMQ
* Master
* Worker
* Reaper

```bash
docker-compose up --build
```

### Send a test job:

```bash
python3 master.py send-test
```

### Watch worker logs:

```bash
docker logs -f worker
```

---

## 🖥️ **Running Without Docker**

### Install dependencies:

```bash
pip3 install -r requirements.txt
```

### Start RabbitMQ:

```bash
sudo service rabbitmq-server start
```

### Run components:

```bash
python3 master.py
python3 worker.py
python3 reaper.py
```

---

## 🗂️ **Project Structure**

```
beseri_distributed_worker/
│
├── master.py          # Sends jobs into RabbitMQ
├── worker.py          # Python worker
├── reaper.py          # Retry/timeout recovery system
│
├── c_worker/          # High-performance C worker
│   ├── worker.c
│   ├── Makefile
│
├── docker-compose.yml
├── Dockerfile.master
├── Dockerfile.worker
│
├── jobs/              # Job handlers
│   ├── image_processor.py
│   ├── analysis.py
│   └── ...
│
├── config.yaml        # Config: retries, timeouts, queues
├── requirements.txt
└── README.md
```

---

## 📝 **Configuration**

Edit `config.yaml`:

```yaml
retries: 5
backoff_seconds: 2
visibility_timeout: 30

queues:
  - image.process
  - analysis.batch
```

---

## 🧪 **Example: Creating a New Job Type**

Add a new file:

`jobs/video_encoder.py`:

```python
def run(payload):
    print("Encoding video:", payload["file"])
```

Then send job from master:

```python
python3 master.py send video.process file=movie.mp4
```

---

## 🌐 **Monitoring**

RabbitMQ Management Panel:

```
http://localhost:15672
user: guest  
pass: guest
```

---

## 🤝 **Contributing**

1. Fork the repo
2. Create a feature branch
3. Write clean, documented code
4. Open a pull request

---

## 📜 **License**

MIT License – free to use, modify, and distribute.

---

- minor update @ 2026-01-10 18:16:25.149898
- minor update @ 2026-01-10 18:16:25.384092
- minor update @ 2026-01-10 18:16:25.837504
- minor update @ 2026-01-10 18:16:26.068634
- minor update @ 2026-01-10 18:16:26.303510
- minor update @ 2026-01-10 18:16:58.258679
- minor update @ 2026-01-10 18:16:58.480131
- minor update @ 2026-01-10 18:16:58.697791
- minor update @ 2026-01-10 18:16:59.353433
- minor update @ 2026-01-10 18:16:59.570373
- minor update @ 2026-01-10 18:17:00.219345
- minor update @ 2026-01-10 18:17:00.440784
- minor update @ 2026-01-10 18:17:01.095715
- minor update @ 2026-01-10 18:17:01.313371
- minor update @ 2026-01-10 18:17:01.751708
- minor update @ 2026-01-10 19:52:11.043065
- minor update @ 2026-01-10 19:52:12.220892
- minor update @ 2026-01-10 19:52:12.454803
- minor update @ 2026-01-10 20:06:32.000709
- minor update @ 2026-01-10 20:06:32.283106
- minor update @ 2026-01-10 20:06:32.548374
- minor update @ 2026-01-10 20:06:32.811596
- minor update @ 2026-01-10 20:06:33.074048
- minor update @ 2026-01-10 20:06:33.328718
- minor update @ 2026-01-10 20:06:34.103959
- minor update @ 2026-01-10 20:06:34.358437
- minor update @ 2026-01-10 20:06:34.614119
- minor update @ 2026-01-10 20:06:34.867212
- minor update @ 2026-01-10 20:06:35.115305
- minor update @ 2026-01-10 20:06:35.367042
- minor update @ 2026-01-10 20:06:35.623780
- minor update @ 2026-01-10 20:06:35.878712
- minor update @ 2026-01-10 20:06:36.132925
- minor update @ 2026-01-10 20:06:36.656647
- minor update @ 2026-01-10 20:06:37.169421
- minor update @ 2026-01-10 20:06:37.430667
- minor update @ 2026-01-10 20:06:37.679602
- minor update @ 2026-01-10 20:06:37.928593
- minor update @ 2026-01-10 20:06:38.184263
- minor update @ 2026-01-10 20:06:38.972049
- minor update @ 2026-01-10 20:06:39.227061
- minor update @ 2026-01-10 20:06:39.993596
- minor update @ 2026-01-11 09:22:32.521020
- minor update @ 2026-01-11 09:22:44.027140
- minor update @ 2026-01-11 11:18:19.854389
- minor update @ 2026-01-11 11:18:24.110432
- minor update @ 2026-01-11 11:18:42.137772
- minor update @ 2026-01-11 11:19:06.172853
- minor update @ 2026-01-11 23:20:41.764358
- minor update @ 2026-01-11 23:21:04.544702
- minor update @ 2026-01-11 23:21:28.280572
- minor update @ 2026-01-11 23:21:44.016037
- minor update @ 2026-01-12 08:34:44.206121
- minor update @ 2026-01-12 08:34:46.469119
- minor update @ 2026-01-12 08:35:04.165938
- minor update @ 2026-01-12 08:35:07.391439
- minor update @ 2026-01-12 08:35:11.613847
- minor update @ 2026-01-12 08:35:25.076486
- minor update @ 2026-01-12 08:35:32.298211
- minor update @ 2026-01-12 09:34:27.681626
- minor update @ 2026-01-12 09:34:29.931922
- minor update @ 2026-01-12 09:34:38.145394
- minor update @ 2026-01-12 09:34:47.578766
- minor update @ 2026-01-12 13:42:48.767353
- minor update @ 2026-01-12 13:43:10.467952
- minor update @ 2026-01-12 13:43:32.389734
- minor update @ 2026-01-12 13:43:34.614818
- minor update @ 2026-01-12 15:27:29.464780
- minor update @ 2026-01-12 15:27:43.273888
- minor update @ 2026-01-12 15:27:47.543891
- minor update @ 2026-01-12 15:27:51.819274
- minor update @ 2026-01-12 21:22:47.435519
- minor update @ 2026-01-12 21:22:50.673724
- minor update @ 2026-01-12 21:22:59.912137
- minor update @ 2026-01-12 21:23:08.137431
- minor update @ 2026-01-12 21:23:16.364893
- minor update @ 2026-01-12 21:23:26.827570
- minor update @ 2026-01-12 21:23:36.065434
- minor update @ 2026-01-12 21:23:53.543079
- minor update @ 2026-01-12 21:24:01.767147
- minor update @ 2026-01-12 21:32:23.518641
- minor update @ 2026-01-12 21:32:27.734453
- minor update @ 2026-01-12 21:32:36.938376
- minor update @ 2026-01-12 22:20:30.664994
- minor update @ 2026-01-12 22:20:40.322724
- minor update @ 2026-01-12 22:20:46.804121
- minor update @ 2026-01-12 22:20:55.360626
- minor update @ 2026-01-12 22:21:05.868884
- minor update @ 2026-01-12 22:21:17.899822
- minor update @ 2026-01-13 10:26:20.368619
- minor update @ 2026-01-13 10:26:46.868299
- minor update @ 2026-01-13 10:26:57.386969
- minor update @ 2026-01-13 10:27:11.974757
- minor update @ 2026-01-13 10:27:18.650567
- minor update @ 2026-01-13 16:33:57.602955
- minor update @ 2026-01-13 16:34:05.898455
- minor update @ 2026-01-13 16:34:31.350423
- minor update @ 2026-01-13 20:27:32.475332
- minor update @ 2026-01-13 20:27:43.110898
- minor update @ 2026-01-13 20:27:57.382100
- minor update @ 2026-01-13 20:28:04.690881
- minor update @ 2026-01-13 20:28:14.986082
- minor update @ 2026-01-13 20:28:24.581004
- minor update @ 2026-01-13 21:23:11.803497
- minor update @ 2026-01-14 05:26:23.332728
- minor update @ 2026-01-14 05:26:29.123840
- minor update @ 2026-01-14 05:26:35.465955
- minor update @ 2026-01-14 05:26:42.718991
- minor update @ 2026-01-14 05:26:49.979420
- minor update @ 2026-01-14 05:26:53.237561
- minor update @ 2026-01-14 05:27:01.739560
- minor update @ 2026-01-14 05:27:04.986013
- minor update @ 2026-01-15 16:37:13.914254
- minor update @ 2026-01-15 16:37:37.543739
- minor update @ 2026-01-15 16:37:39.835064
- minor update @ 2026-01-15 18:38:31.847720
- minor update @ 2026-01-16 14:25:13.966605
- minor update @ 2026-01-16 14:25:29.862680
- minor update @ 2026-01-16 14:25:38.133107
- minor update @ 2026-01-16 14:25:42.399023
- minor update @ 2026-01-16 14:25:48.661704
- minor update @ 2026-01-16 14:25:50.932085
- minor update @ 2026-01-16 19:20:32.268662
- minor update @ 2026-01-16 19:20:39.574034
- minor update @ 2026-01-16 19:20:43.850855
- minor update @ 2026-01-16 19:20:46.121199
- minor update @ 2026-01-16 19:20:52.398580
- minor update @ 2026-01-16 19:20:57.681651
- minor update @ 2026-01-16 19:21:11.217285
- minor update @ 2026-01-16 19:21:20.492872
- minor update @ 2026-01-17 01:45:30.751890
- minor update @ 2026-01-17 01:45:53.921526
- minor update @ 2026-01-17 09:21:45.646552
- minor update @ 2026-01-17 09:22:04.198966
- minor update @ 2026-01-17 09:22:13.732249
- minor update @ 2026-01-17 09:22:22.651351
- minor update @ 2026-01-17 09:22:37.228686
- minor update @ 2026-01-17 13:29:18.352474
- minor update @ 2026-01-17 13:29:45.875710
- minor update @ 2026-01-17 22:20:54.839255
- minor update @ 2026-01-17 22:21:04.114426
- minor update @ 2026-01-17 22:21:06.380130
- minor update @ 2026-01-17 22:21:28.181907
- minor update @ 2026-01-18 15:20:50.220574
- minor update @ 2026-01-18 15:20:55.475858
- minor update @ 2026-01-18 15:21:32.795810
- minor update @ 2026-01-18 15:21:35.121628
- minor update @ 2026-01-18 15:21:38.383451
- minor update @ 2026-01-18 18:29:53.580079
- minor update @ 2026-01-18 18:29:57.874789
- minor update @ 2026-01-18 18:30:01.181214
- minor update @ 2026-01-18 18:30:09.482967
- minor update @ 2026-01-18 18:30:13.782008
- minor update @ 2026-01-18 18:30:28.733292
- minor update @ 2026-01-18 18:30:35.320825
- minor update @ 2026-01-19 18:34:11.638323
- minor update @ 2026-01-19 18:34:14.214306
- minor update @ 2026-01-19 18:34:42.550095
- minor update @ 2026-01-20 18:38:58.723134
- minor update @ 2026-01-20 18:39:09.280228
- minor update @ 2026-01-20 18:39:20.511164
- minor update @ 2026-01-20 18:39:27.814175
- minor update @ 2026-01-20 23:24:33.531024
- minor update @ 2026-01-20 23:24:35.778193
- minor update @ 2026-01-20 23:24:46.033119
- minor update @ 2026-01-20 23:25:03.055327
- minor update @ 2026-01-21 03:45:23.560980
- minor update @ 2026-01-21 03:45:25.904393
- minor update @ 2026-01-21 17:55:26.509883
- minor update @ 2026-01-21 17:55:34.835308
- minor update @ 2026-01-21 17:55:43.157691
- minor update @ 2026-01-21 17:56:08.104249
- minor update @ 2026-01-22 01:54:15.414454
- minor update @ 2026-01-22 01:54:20.684586
- minor update @ 2026-01-22 01:54:23.946316
- minor update @ 2026-01-22 12:53:12.294775
- minor update @ 2026-01-22 12:53:45.249314
- minor update @ 2026-01-22 12:53:52.749834
- minor update @ 2026-01-22 12:54:08.255497
- minor update @ 2026-01-22 12:54:12.503400
- minor update @ 2026-01-22 15:32:43.788765
- minor update @ 2026-01-22 15:33:01.654994
- minor update @ 2026-01-22 15:33:18.220046
- minor update @ 2026-01-22 16:37:08.189848
- minor update @ 2026-01-22 16:37:27.035565
- minor update @ 2026-01-22 16:37:50.839836
- minor update @ 2026-01-22 16:38:13.915925
- minor update @ 2026-01-23 17:26:18.011277
- minor update @ 2026-01-23 17:26:26.636016
- minor update @ 2026-01-24 06:33:35.916428
- minor update @ 2026-01-24 06:33:44.844850
- minor update @ 2026-01-24 08:28:40.034711
- minor update @ 2026-01-24 08:28:45.538528
- minor update @ 2026-01-24 11:18:55.256785
- minor update @ 2026-01-24 11:18:57.800577
- minor update @ 2026-01-24 11:19:03.305000
- minor update @ 2026-01-24 11:19:23.034053
- minor update @ 2026-01-24 11:19:32.297716
- minor update @ 2026-01-25 08:29:32.006857
- minor update @ 2026-01-25 08:29:47.128906
- minor update @ 2026-01-25 23:21:12.111069
- minor update @ 2026-01-25 23:21:28.691700
- minor update @ 2026-01-25 23:21:31.975204
- minor update @ 2026-01-26 06:39:23.579641
- minor update @ 2026-01-26 06:40:11.190857
- minor update @ 2026-01-26 10:28:59.133038
- minor update @ 2026-01-26 10:29:03.192365
- minor update @ 2026-01-26 10:29:31.810277
- minor update @ 2026-01-27 18:41:04.531888
- minor update @ 2026-01-27 18:41:14.075024
- minor update @ 2026-01-27 18:41:29.592588
- minor update @ 2026-01-27 18:41:31.855024
- minor update @ 2026-01-27 18:41:47.661045
- minor update @ 2026-01-27 21:19:00.472057
- minor update @ 2026-01-27 21:19:15.486667
- minor update @ 2026-01-28 15:34:29.634333
- minor update @ 2026-01-28 15:34:33.364977
- minor update @ 2026-01-28 15:34:37.665716
- minor update @ 2026-01-28 23:27:50.199149
- minor update @ 2026-01-28 23:27:59.480037
- minor update @ 2026-01-28 23:28:33.200044
- minor update @ 2026-01-28 23:28:37.478905
- minor update @ 2026-01-29 04:27:37.519527
- minor update @ 2026-01-29 04:27:40.207982
- minor update @ 2026-01-29 04:27:52.196565
- minor update @ 2026-01-29 13:00:21.623611
- minor update @ 2026-01-29 13:01:10.477635
- minor update @ 2026-01-29 16:45:36.031536
- minor update @ 2026-01-29 16:45:50.155845
- minor update @ 2026-01-30 14:47:39.402419
- minor update @ 2026-01-30 14:47:46.969025
- minor update @ 2026-01-30 16:41:32.897943
- minor update @ 2026-01-30 23:26:59.831695
- minor update @ 2026-01-30 23:27:08.122501
- minor update @ 2026-01-30 23:27:10.386001
- minor update @ 2026-01-31 08:32:40.646335
- minor update @ 2026-01-31 08:32:48.143702
- minor update @ 2026-01-31 08:32:52.611505
- minor update @ 2026-02-01 15:26:46.451052
- minor update @ 2026-02-01 19:25:23.511094
- minor update @ 2026-02-02 13:02:39.890388
- minor update @ 2026-02-02 13:02:51.145891
- minor update @ 2026-02-02 16:42:07.796946
- minor update @ 2026-02-02 16:42:14.284038
- minor update @ 2026-02-03 07:43:44.323666
- minor update @ 2026-02-03 07:43:57.263349
- minor update @ 2026-02-03 10:41:14.865947
- minor update @ 2026-02-03 10:41:25.586874
- minor update @ 2026-02-03 15:51:39.349402
- minor update @ 2026-02-03 15:51:45.018742
- minor update @ 2026-02-03 15:51:55.796359
- minor update @ 2026-02-03 15:52:03.383977
- minor update @ 2026-02-03 22:31:34.532960
- minor update @ 2026-02-03 22:31:38.795560
- minor update @ 2026-02-04 19:39:25.786799
- minor update @ 2026-02-05 08:44:54.667038
- minor update @ 2026-02-05 08:45:09.006491
- minor update @ 2026-02-05 11:36:12.209440
- minor update @ 2026-02-05 17:50:09.322965
- minor update @ 2026-02-06 06:57:08.583623
- minor update @ 2026-02-06 06:57:14.871923
- minor update @ 2026-02-06 14:39:36.178403
- minor update @ 2026-02-06 14:40:00.095773
- minor update @ 2026-02-07 23:31:07.954832
- minor update @ 2026-02-08 20:29:41.399666
- minor update @ 2026-02-09 07:05:52.630356
- minor update @ 2026-02-09 07:05:57.609389
- minor update @ 2026-02-09 07:06:01.896072
- minor update @ 2026-02-09 08:55:19.632358
- minor update @ 2026-02-09 08:55:24.170986
- minor update @ 2026-02-09 08:55:36.286699
- minor update @ 2026-02-09 22:37:32.398103
- minor update @ 2026-02-09 22:38:08.520139
- minor update @ 2026-02-10 10:06:05.200617
- minor update @ 2026-02-10 20:56:32.159094
- minor update @ 2026-02-10 20:57:03.373960
- minor update @ 2026-02-11 02:30:11.564105
- minor update @ 2026-02-11 02:30:17.818186
- minor update @ 2026-02-11 10:52:18.071019
- minor update @ 2026-02-11 10:52:29.582404
- minor update @ 2026-02-11 10:52:40.337737
- minor update @ 2026-02-11 22:30:35.373555
- minor update @ 2026-02-12 06:09:28.249390
- minor update @ 2026-02-12 06:09:45.902437
- minor update @ 2026-02-13 04:54:12.120632
- minor update @ 2026-02-13 04:54:20.971582
- minor update @ 2026-02-13 04:54:25.250275
- minor update @ 2026-02-14 07:34:32.509747
- minor update @ 2026-02-14 07:34:58.531662
- minor update @ 2026-02-14 08:35:28.159403
- minor update @ 2026-02-14 17:26:20.660590
- minor update @ 2026-02-14 17:26:26.442559
- minor update @ 2026-02-16 11:41:13.250258
- minor update @ 2026-02-16 11:41:19.838164
- minor update @ 2026-02-16 11:41:39.431497
- minor update @ 2026-02-18 04:54:01.744568
- minor update @ 2026-02-18 18:56:55.569836
- minor update @ 2026-02-18 23:31:10.951900
- minor update @ 2026-02-18 23:31:23.345946
- minor update @ 2026-02-19 02:22:13.999639
- minor update @ 2026-02-19 11:38:46.741123
- minor update @ 2026-02-19 11:39:06.998924
- minor update @ 2026-02-19 13:09:15.726512
- minor update @ 2026-02-19 14:49:24.599614
- minor update @ 2026-02-19 14:49:36.815245
- minor update @ 2026-02-19 16:54:59.695435
- minor update @ 2026-02-19 16:55:17.901612
- minor update @ 2026-02-20 04:47:56.848519
- minor update @ 2026-02-22 12:52:46.150961
- minor update @ 2026-02-23 21:46:50.503881
- minor update @ 2026-02-23 21:46:59.803828
- minor update @ 2026-02-24 09:54:29.272419
- minor update @ 2026-02-24 09:54:47.455968
- minor update @ 2026-02-24 19:04:05.487335
- minor update @ 2026-02-24 19:04:24.700049
- minor update @ 2026-02-24 19:04:26.944256
- minor update @ 2026-02-24 19:04:46.134743
- minor update @ 2026-02-24 21:36:29.260238
- minor update @ 2026-02-25 14:51:03.329079
- minor update @ 2026-02-27 06:56:37.883286
- minor update @ 2026-02-27 22:24:42.803397
- minor update @ 2026-02-27 23:26:04.677862
- minor update @ 2026-02-27 23:26:07.921716
- minor update @ 2026-02-28 04:00:14.376391
- minor update @ 2026-02-28 04:00:21.629359
- minor update @ 2026-02-28 08:31:29.624785
- minor update @ 2026-02-28 11:20:10.887509
- minor update @ 2026-03-01 11:21:13.550977
- minor update @ 2026-03-01 11:21:18.846815
- minor update @ 2026-03-01 18:35:52.082966
- minor update @ 2026-03-02 05:53:32.238092
- minor update @ 2026-03-02 07:00:08.222849
- minor update @ 2026-03-03 08:42:52.193302
- minor update @ 2026-03-03 20:34:26.285064
- minor update @ 2026-03-03 21:35:17.233109
- minor update @ 2026-03-04 10:38:08.205427
- minor update @ 2026-03-04 11:31:33.839809
- minor update @ 2026-03-04 12:59:53.527023
- minor update @ 2026-03-04 15:42:09.905348
- minor update @ 2026-03-04 15:42:27.138030
- minor update @ 2026-03-04 16:47:26.086659
- minor update @ 2026-03-04 16:47:39.236734
- minor update @ 2026-03-05 06:54:20.786428
- minor update @ 2026-03-05 08:43:37.403775
- minor update @ 2026-03-05 08:43:43.180564
- minor update @ 2026-03-05 08:43:54.093270
- minor update @ 2026-03-05 15:52:04.261633
- minor update @ 2026-03-06 13:58:44.644212
- minor update @ 2026-03-06 13:58:54.234483
- minor update @ 2026-03-06 15:38:59.019126
- minor update @ 2026-03-06 15:39:21.468873
- minor update @ 2026-03-06 20:33:49.422466
- minor update @ 2026-03-07 10:25:38.881630
- minor update @ 2026-03-07 18:35:48.500529
- minor update @ 2026-03-07 18:35:53.743125
- minor update @ 2026-03-07 20:27:30.031781
- minor update @ 2026-03-07 20:27:53.423419
- minor update @ 2026-03-08 11:21:58.278996
- minor update @ 2026-03-08 11:22:24.865272
- minor update @ 2026-03-08 11:22:37.062683
- minor update @ 2026-03-08 17:24:09.971071
- minor update @ 2026-03-08 17:24:26.250126
- minor update @ 2026-03-08 17:24:34.506469
- minor update @ 2026-03-09 20:36:35.897085
- minor update @ 2026-03-11 15:50:45.773171
- minor update @ 2026-03-11 15:51:17.165963
- minor update @ 2026-03-11 15:51:35.363983
- minor update @ 2026-03-11 19:41:55.662502