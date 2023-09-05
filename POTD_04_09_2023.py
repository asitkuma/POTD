 def check(self,i,j,n,m,mat):
        if i >= 0 and i < n and j >= 0 and j < m and mat[i][j]=='O':
            return True
        return False

    def recur(self,l1,mat,i,j,n,m):
        if l1[i][j]==-1:
            return
        l1[i][j]=-1 #visited
        if self.check(i,j-1,n,m,mat):
            self.recur(l1,mat,i,j-1,n,m)
        if self.check(i,j+1,n,m,mat):
            self.recur(l1,mat,i,j+1,n,m)
        if self.check(i-1,j,n,m,mat):
            self.recur(l1,mat,i-1,j,n,m)
        if self.check(i+1,j,n,m,mat):
            self.recur(l1,mat,i+1,j,n,m)
       
        
    def fill(self, n, m, mat):
        l1=[[1 for i in range(m)].copy() for i in range(n)]
        for i in range(1):
            for j in range(m):
                if mat[i][j]=='O':
                    self.recur(l1,mat,i,j,n,m)
            for j in range(n):
                if mat[j][i]=='O':
                    self.recur(l1,mat ,j ,i ,n, m)
            for j in range(m):
                if mat[n-1][j]=='O':
                    self.recur(l1,mat,n-1,j,n,m)
            for j in range(n):
                if mat[j][m-1]=='O':
                    self.recur(l1,mat,j,m-1,n,m)
        for i in range(n):
            for j in range(m):
                if mat[i][j]=='O' and l1[i][j]==1:
                    mat[i][j]='X'
        return mat


