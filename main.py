from sys import stdin
from math import sqrt


class Pipe:

    def __init__(self, next, flow, sp):
        self.next = next                                # Ansätter var pipen går
        self.flow = flow / 100                          # Ansätter hur många % mat som passerar, gör till decimal för att kunna räkna med
        self.sp = sp                                    # 1 om superkraft, annars 0
        self.leaf = -1                                  # -1 och förälder, annars värdet på hur mycket mat lövet behöver


def read(t):
    N = int(stdin.readline())                           # Läser in första raden i inputen, N
    for i in range(0, N-1):                             # Läser in de N kommande raderna och skapar noder som sparas i en lista
        new_line = stdin.readline().strip().split(" ")
        A = int(new_line[0]) - 1                        # -1 pga vill använda som index
        B = int(new_line[1]) - 1
        X = int(new_line[2])
        T = int(new_line[3])
        t[B] = Pipe(A, X, T)
    index = 0
    for x in stdin.readline().strip().split(" "):       # Läser in den sista raden med info om löven
        if t[index] is not None:                        # Lägger till info om alla löven i deras pipe-objekt
            t[index].leaf = int(x)
        index += 1
    stdin.close()
    return


def needs_the_most(tree):
    leafs = []                                          # Skapar en lista med alla löven
    for node in tree:                                   # Itererar över hela trädet
        if node is not None:                            # Identifierar om node är ett objekt eller inte
            if node.leaf != -1:                         # Hittar löven och lägger till dem i listan leafs
                leafs.append(node)
    paths = []                                          # Skapar en lista där info om hur mycket total L varje löv kräver
    for node in leafs:                                  # Räknar för varje löv ut vägen till toppen
        value = 0
        while node:                                     # Itererar över alla noder upp till toppen. Avbryter när toppen är nådd då den är None
            if node.leaf != -1:                         # Om noden är ett löv sätter vi värdet till lövets värde
                value = node.leaf
            if node.sp == 1 and value >= 1:             # Kollar om noden har superkraft och tar isf roten ur
                value = sqrt(value)                     # Kollar även om värdet är större än 1 för annars finns ingen vits med att ha superkrafter på
            value = value / node.flow                   # Dividerar värdet med pipens flow
            node = tree[node.next]                      # Ansätter node till den kommande noden på vägen mot toppen
        paths.append(value)                             # Lägger till värdet för vad detta lövet kräver för total L
    return "%.4f" % max(paths)                          # När alla vägar gåtts igenom returneras det högsta värdet i paths då det defininerar den minsta mängden L för att alla myror ska bli mätta. %.4f avrundar till 4 decimaler


def main():
    MaxN = 1000                                         # Max antal noder trädet får innehålla
    tree = [None] * MaxN                                # Skapar trädet med max antal platser
    read(tree)                                          # Läser in all input och sparar på rätt ställe
    return needs_the_most(tree)                         # Räknar ut och returnerar det minsta möjliga L-värdet


if __name__ == '__main__':
    print(main())
