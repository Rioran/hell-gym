# hell-gym
Command line application for hell gym operation.

Trainers must register themselves. Trainer can voluntarely get new client from the queue. Trainer can set booking status for client as finished.

Clients can join the booking queue.

## commands help

```bash
python -m gym.main --help
```

## test db creation

- prefill fills database with a few objects
- trainers prints out recent trainers

```bash
python -m gym.main --prefill --trainers
```

## list last entries

```bash
python -m gym.main --trainers
```

```bash
python -m gym.main --bookings
```

```bash
python -m gym.main --updates
```

## add entities
Trainers:
```bash
python -m gym.main --register-trainer "Mister Bin" "Abused the Queen image for quite some time"
```
```bash
python -m gym.main --register-trainer "Zena the Queen" "Во времена богов, воителей и королей простой народ искал защиты..."
```
Bookings:
```bash
python -m gym.main --new-booking "Alfred Enstien"
```

## TODO list
- [X] add terminal command **--register-trainer trainer_name [trainer_bio]**, Gosh
- [X] add crud function to add trainer to the database, Danya
- [X] add terminal command **--ask-for-client trainer_name**, Layla
- [x] add crud function to ask for a client: check if trainer is available / check if clients are available, Dima
- [x] add terminal command **--finish-client trainer_name**, Gevorg
- [ ] add crud function to change client status to finished
- [x] add terminal command **--new-booking** to add new client to the queue, Danya
- [x] add crud function to add new booking, Danya
