import sys
class Maze():
    def __init__(self, filename):
        self.labirinto = []
        for line in open(filename):
            new_line = list(line.strip('\n'))
            for character in new_line:
                if character not in [' ', '+', 'S', 'E', '-', '|']:
                    print("ERRO, Elemento NÃO reconhecido!")
            self.labirinto.append(new_line)
        self.simplificacao()
        self.traducao()

    def print_labirinto(self):
        for row in self.oficial:
            print("".join(str(character) for character in row))
    def largura(self):
        return(len(self.oficial[0]))
    def altura(self):
        return(len(self.oficial))
    def simplificacao(self):
        self.trad = self.labirinto
        self.new_lab = []
        for row_index, row in enumerate(self.trad):
            new_row = []
            for col_index, col in enumerate(row):
                if col == '+':
                    if col_index == 0:
                        new_row.append(self.trad[row_index][col_index])
                        new_row.append(self.trad[row_index][col_index+2])
                    elif col_index == len(self.labirinto[0]) - 1:
                        new_row.append(self.trad[row_index][col_index])
                    else:
                        new_row.append(self.trad[row_index][col_index])
                        new_row.append(self.trad[row_index][col_index+2])
                elif row_index == len(self.labirinto) - 1: pass
                elif self.trad[row_index+1][col_index] == '+':
                    if col_index == 0:
                        new_row.append(self.trad[row_index][col_index])
                        new_row.append(self.trad[row_index][col_index+2])
                    elif col_index == len(self.labirinto[0]) - 1:
                        new_row.append(self.trad[row_index][col_index])
                    else:
                        new_row.append(self.trad[row_index][col_index])
                        new_row.append(self.trad[row_index][col_index+2])
                else:
                    pass
            self.new_lab.append(new_row)
    def traducao(self):
        self.oficial = []
        for row_index, row in enumerate(self.new_lab):
            temp = []
            for col_index, col in enumerate(row):
                if col in ['+', '-', '|']:
                    temp.append(1)
                elif col == 'S': temp.append(2)
                elif col == 'E': temp.append(3)
                else: temp.append(0)
            self.oficial.append(temp)
    def labirinto_traduzido(self):
        return self.oficial

    def entrada_labirinto(self): #start
        copia_labirinto = self.oficial
        pos = []
        for row_index, row in enumerate(copia_labirinto):
            for col_index, col in enumerate(row):
                if col == 2:
                    pos.append(row_index)
                    pos.append(col_index)
                    break
        return pos

    def saida_labirinto(self): #end
        copia_labirinto = self.oficial
        pos = []
        for row_index, row in enumerate(copia_labirinto):
            for col_index, col in enumerate(row):
                if col == 3:
                    pos.append(row_index)
                    pos.append(col_index)
                    break
        return pos
    def retorna_pos_caminhos(self):
        copia_labirinto = self.oficial
        possiveis_caminhos = []
        for row_index, row in enumerate(copia_labirinto):
            for col_index, col in enumerate(row):
                if col == 0 or col == 3:
                    possiveis_caminhos.append([row_index, col_index])
        return possiveis_caminhos