listDosen = [
    "Terima kasih banyak atas pengajaran yang sangat bermanfaat. Penjelasan Bapak/Ibu sangat jelas dan mudah dipahami.",
    "Saya sangat menghargai dedikasi Bapak/Ibu dalam memberikan bimbingan selama semester ini. Terima kasih atas ilmu yang diberikan.",
    "Pelajaran ini membantu saya memahami konsep dengan lebih baik. Saya menghargai cara Bapak/Ibu mendekatkan materi kepada mahasiswa.",
    "Bapak/Ibu adalah seorang dosen yang ramah dan selalu siap membantu. Saya merasa nyaman belajar di kelas ini.",
    "Materi perkuliahan sangat relevan dengan perkembangan terkini di bidang ini. Saya merasa lebih siap menghadapi tantangan di masa depan.",
    "Bapak/Ibu memiliki cara mengajar yang interaktif dan melibatkan mahasiswa. Terima kasih atas suasana belajar yang menyenangkan.",
    "Saya senang dengan feedback yang konstruktif dan membantu dalam meningkatkan kualitas pekerjaan saya. Terima kasih atas bimbingan Bapak/Ibu.",
    "Kuliah ini memberikan wawasan baru bagi saya. Saya menyukai pendekatan praktis yang diterapkan dalam setiap pertemuan.",
    "Bapak/Ibu sangat sabar dan responsif terhadap pertanyaan mahasiswa. Ini membuat saya lebih percaya diri dalam belajar.",
    "Terima kasih atas saran-saran pembelajaran yang membantu saya meningkatkan keterampilan dan pemahaman saya.",
    "Saya merasa terinspirasi oleh dedikasi Bapak/Ibu terhadap bidang ini. Terima kasih telah berbagi pengetahuan dan pengalaman.",
    "Kuliah ini memberikan pemahaman yang mendalam tentang topik tersebut. Saya merasa lebih siap mengambil langkah selanjutnya dalam karier saya.",
    "Saya senang dengan pendekatan pembelajaran yang menciptakan minat dan antusiasme dalam belajar.",
    "Bapak/Ibu memberikan umpan balik yang konstruktif dan membantu saya mengidentifikasi area yang perlu diperbaiki. Terima kasih atas bimbingan tersebut.",
    "Pelajaran ini tidak hanya memberikan teori tetapi juga aplikasi praktis yang berguna untuk karier saya di masa depan. Saya sangat bersyukur menjadi mahasiswa Bapak/Ibu."
];

var listCourse = [
    "Terima kasih atas kursus ini yang memberikan pemahaman mendalam tentang subjek ini. Saya merasa lebih siap untuk menghadapi tantangan di masa depan.",
    "Kursus ini sangat relevan dengan kebutuhan industri saat ini. Materi-materi yang diajarkan sangat berguna untuk pengembangan keterampilan.",
    "Saya menghargai pendekatan praktis dalam kursus ini. Pelajaran yang saya dapatkan dapat langsung saya terapkan dalam pekerjaan sehari-hari.",
    "Terima kasih atas bimbingan dan dukungan selama kursus ini. Ini memberikan nilai tambah yang signifikan pada pengalaman belajar saya.",
    "Materi kursusnya terstruktur dengan baik dan mudah diakses. Ini memudahkan saya untuk mengikuti perkembangan materi secara sistematis.",
    "Saya senang dengan variasi metode pengajaran yang diterapkan dalam kursus ini. Ini membuat pembelajaran menjadi lebih menarik dan tidak monoton.",
    "Kursus ini memberikan pemahaman yang menyeluruh tentang topik tersebut. Saya merasa lebih percaya diri dalam mengaplikasikan pengetahuan ini di dunia nyata.",
    "Saya senang dengan fleksibilitas waktu dalam kursus ini, memungkinkan saya untuk menyesuaikan pembelajaran dengan jadwal harian saya.",
    "Materi kursusnya sangat terkini dan mencakup perkembangan terbaru di bidang ini. Ini menciptakan kesan bahwa kursus ini selalu up-to-date.",
    "Saya menghargai adanya proyek atau tugas praktis yang menguji pemahaman dan keterampilan yang telah saya pelajari.",
    "Kursus ini membuka wawasan saya tentang potensi karier di bidang ini. Terima kasih atas arahan dan informasi yang berharga.",
    "Saya merasa kursus ini memberikan nilai tambah yang besar pada pendidikan saya. Saya merasa lebih siap untuk menghadapi tantangan di pasar kerja.",
    "Metode penilaian yang adil dan transparan membuat saya merasa bahwa saya dinilai secara objektif dan adil.",
    "Kursus ini tidak hanya fokus pada teori, tetapi juga memberikan pandangan praktis yang sangat diperlukan dalam dunia kerja.",
    "Kursus ini memberikan kesempatan untuk berkolaborasi dengan sesama peserta kursus, yang menambah nilai sosial dalam pengalaman belajar saya."
];

function getRandomChoice(array) {
    if (Array.isArray(array) && array.length > 0) {
      const randomIndex = Math.floor(Math.random() * array.length);
      return array[randomIndex];
    } else {
      console.error('Error: Invalid input. Please provide a non-empty array.');
      return null;
    }
  }

function kuisionerIpd(range) {
    let type = document.getElementById("MK11")? "MK" : "DO";
    for(i = 1; i <= 10; i++) document.querySelector("input#"+type+i+(Math.floor(Math.random()*(range[1]-range[0]+1)) + range[0])).click();
    document.querySelector("#txtKomentar").value = type == "MK"?getRandomChoice(listCourse):getRandomChoice(listDosen); document.querySelector('#chkPermanent').checked = true;
}

kuisionerIpd([3,4]);

