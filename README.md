# python-music
let your computer great music for you, inspired by classical music and using pyudio library.

### The concept
the first part of the code generates two outputs:
- sequence of integers representing musical notations
- sequence of floats representing the duration of the note

Both have the same length.

### Notes Sequence
The notes squences are divided into different blocks. Those blocks are:
- scale
- arpeggio
- pentatonic
- augmented
- diminshed 

The final sequence is a combination of those blocks with randomness and shuffle. There is a different probability for each of those:
- the selected block of *notes sequence*
- length of the block (how many notes to use)
- starting point of the sequence
- shuffle within the block
- major or minor sequence
- ascending and/or decending the block
- duration of some notes
- repetition of a block
- the next block of *notes sequence*

example:
```
randomly select major or minor
rn  0 means minor, if 1 then major
rn = 1
random block selected: arpeggio 
ar = [0,3+rn,7,12,15+rn,19,24,27+rn]
random starting point and length
ar = [12, 16, 19,24, 27]
probability of adding a decending version to it
ar = [12, 16, 19, 24, 27, 24, 19, 16, 12]
probability of shuffle
ar = [ 12, 16, 19, 24, 19, 24, 27, 16, 12]
Another array is generated for the duration of the note
leng1 = [.13, .13, .13, .13, .13, .13, .13, .13, .26] 
randomly select the next block and so on
```

Each time you run the code, a new music is generated.

## Music Player
I'm using here pyaudio
I'm assuming 0 in the sequence is A4 (440Hz). The other notes are calcualted from this assumptions.
A harmony is added to give the music a better taste and colors at frequency of 330Hz E4
