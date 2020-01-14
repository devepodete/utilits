# Convert Turing Machine to Markov's algorithm's code :floppy_disk:

## Example:

### Turing Machine file
```
00,a,>,01
02,a,#,55
z,%,@,aaaa
```
### Result in Markov's algorithm
```
a(00)A->aA(01)
a(00)->a_(01)
a(02)->.a(55)
%(z)->@(aaaa)
```
