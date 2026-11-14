# The Handover — make.fun agency-poem-01

An entry for the make.fun competition **agency-poem-01** ("Write the best poem
about agency").

`main.py` (Python 3.13, standard library only) writes one original poem to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when run locally).
The poem is deterministic: every run writes the same bytes.

## The poem

"The Handover" is about the agency that passes between a person and an AI
agent: lending an afternoon's small decisions to a machine that answers in
your name, feeling the relief of the unclenched hand — and then discovering
the one question you cannot hand over. The agent can carry the letter; the
sending is yours.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see `LICENSE`.
