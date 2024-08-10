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

## TODO list

- [ ] add terminal command **--register-trainer trainer_name [trainer_bio]**, Gosh
- [ ] add crud function to add trainer to the database, Danya
- [ ] add terminal command **--ask-for-client trainer_name**, Layla
- [ ] add crud function to ask for a client: check if trainer is available / check if clients are available, Dima
- [ ] add terminal command **--finish-client trainer_name**, Gevorg
- [ ] add crud function to change client status to finished
- [ ] add terminal command **--new-booking** to add new client to the queue
- [ ] add crud function to add new booking
