song = int(input())
notes = set(input().split())
scales = {'A': {'G#', 'E', 'C#', 'F#', 'A', 'D', 'B'},
        'A#': {'D#', 'F', 'C', 'A', 'A#', 'D', 'G'}, 
        'B': {'G#', 'D#', 'E', 'C#', 'F#', 'A#', 'B'}, 
        'C': {'F', 'E', 'C', 'A', 'D', 'G', 'B'}, 
        'C#': {'G#', 'D#', 'F', 'C', 'C#', 'F#', 'A#'}, 
        'D': {'E', 'C#', 'F#', 'A', 'D', 'G', 'B'}, 
        'D#': {'G#', 'D#', 'F', 'C', 'A#', 'D', 'G'}, 
        'E': {'G#', 'D#', 'E', 'C#', 'F#', 'A', 'B'}, 
        'F': {'F', 'E', 'C', 'A', 'A#', 'D', 'G'}, 
        'F#': {'G#', 'D#', 'F', 'C#', 'F#', 'A#', 'B'}, 
        'G': {'E', 'C', 'F#', 'A', 'D', 'G', 'B'}, 
        'G#': {'G#', 'D#', 'F', 'C', 'C#', 'A#', 'G'}}
foundscale = []
for scale in scales:
    if notes.issubset(scales[scale]):
        foundscale.append(scale)
if len(foundscale)!=0:
    print(*sorted(foundscale),sep='\n')
else:
    print('none')