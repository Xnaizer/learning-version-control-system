# Creating

# - git init = sebelum melakukan pengiriman data dan pengambilan data untuk folder yang diinginkan, buatlah repository terlebih dahulu di github/gitlab.., 


# setelahnya, lakukan git init untuk mendownload folder yang berisi methods yang membantu saat melakukan pengiriman data dan pengambilan data. ke cmd -> masuk ke folder yang diinginkan dan ketik git init


# - git clone = mengclone atau menirukan atau mengambil data dari github/gitlab yang sudah diupload, git clone <link repository terkait>


# Make Changes

# - git add nama_file = ketika kita ingin menambahkan file yang baru dan belum diupload maka kita harus menambahkannya ke berangkas atau cart sebelum dikirim. jika menggunakan code git add namafiles berarti kita akan melakukan transfer file yang dipilih


# - git add . = ini digunakan untuk melakukan atau menabahkan semua file yang ada di folder ke berangkas sebelum dikirim 


# - git commit -m "message" = git commit berarti kamu sudah yakin untuk melakukan pengiriman file yang sudah di add, maka buatlah message tambahan untuk memberikan pesan update yang sudah dilakukan


# - git reset nama_file = ketika sudah melakukan commit dan sebelum dipush, ketika ada file yang ingin tidak di commit maka lakukanlah dengan reset.


# - git reset --hard = menghapus semua(semua file) perubahan lokal yang belum di-commit di working directory dan staging area, serta mengatur ulang repositori ke commit tertentu.

# - git reset --hard kode_hash = ketika kita punya versi 1 2 3 4 dan v4 ini sangat tidak efesien maka kita mau kembali ke v3, bisa kalo kita mau ngubah 1 per 1 dari v4 ke v3 tapi bakalan lama, jadi gunakan git log untuk melihat perubahan yang dimau, contoh ambil kode hash v3 dan lakukan reset ke git reset --hard(paksa ubah) kode_hash = maka file akan kembali ke v3

# - git restore nama_file = pada saat git status dimana terdapat file yang di modified, jika didalam modified terdapat satu file yang tidak ingin di commit dan pengen dikembalikan ke awal bisa lakukan git restore maka file akan seperti sebelum di edit.
# - git restore -s namafile = s disini mengembalikan file yang sudah dicommit belum di push (stagged files) kembali ke working files ( folder kita ) sebelum di commit

# Observe
# - git status = memeriksa hal hal yang berubah pada berangkas folder


# - git diff = melihat perubahan yang terjadi pada file di terminal "diff --git a/namafile.exe b/namafile.exe"


# - git show = git-show is a command line utility that is used to view expanded details on Git objects such as blobs, trees, tags, and commits.


# - git log = melihat status perubahan pada file atau yang terjadi pada branch di server
# - git log --oneline = mempermudah pembacaan log



# Sync 

# - git push = setelah commit selesai maka kirimkan ke server ya dengan git push


# - git pull = Mengambil (fetch) perubahan terbaru dari repositori remote dan langsung menggabungkannya (merge) ke branch aktif.


# - git fetch = Mengambil (download) semua perubahan terbaru dari repositori remote ke repositori lokal, tanpa menggabungkannya ke branch aktif.

# Branch
# - git branch = mengecek lintasan apa saja yang tersedia
# - git branch nama = membuat lintasan bernama 'nama'
# - git branch -d nama = menghapus branch yang bernama 'nama'
# - git checkout -b <nama-branch> = jika kamu ingin langsung berpindah ke branch tersebut setelah membuatnya atau git switch -c <nama-branch>

# - git switch feature-login = berpindah ke branch baru

# - git checkout = command untuk berpindah branch atau jalur atau lintasan

# - git revert = dimana ktika kita menggunakan git reset lalu balik ke versi sebelumnya yaitu ke v2 maka v3 v4 v5 akan kehapus, oleh karena itu supaya bisa balik ke v3 tanpa menghapus maka gunakan revert namun kita perlu mengatur conflict yang ada pada v5 dengan v6 yang mana ini adalah commit yang baru. 


# - git merge = untuk menyatukan branch atau lintasan atau jalur 


# - git tag = menandai versi v.1.0.2.3 = git tag -a "v1.0"

# - git push origin master --tags = untuk ngepush tags versi baru


# - U untrack = belum di commit
# - D deleted = dihapus
# - M modified = diubah

# function main() #adding for commit purpose