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