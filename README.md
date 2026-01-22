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