import uuid
from datetime import datetime, timezone

def MOCK_TYPE(tipe: str, level: str) -> dict:
    # Definisi mock HTML string untuk tipe game
    mock_game_html = """<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        #game-container { border: 2px solid #ccc; padding: 20px; border-radius: 8px; max-width: 400px; margin: auto; background-color: #f9f9f9; }
        .btn { padding: 10px 20px; margin: 5px; cursor: pointer; border-radius: 4px; border: 1px solid #007bff; background-color: #007bff; color: white; }
        .btn:hover { background-color: #0056b3; }
        #result { margin-top: 15px; font-weight: bold; }
    </style>
</head>
<body>
    <div id="game-container">
        <h2>Quest: Persamaan Linear</h2>
        <p>Selesaikan persamaan berikut:</p>
        <p id="question"><strong>2x + 5 = 15</strong></p>
        <p>Berapakah nilai x?</p>
        <button class="btn" onclick="checkAnswer(4)">x = 4</button>
        <button class="btn" onclick="checkAnswer(5)">x = 5</button>
        <button class="btn" onclick="checkAnswer(10)">x = 10</button>
        <p id="result"></p>
    </div>
    <script>
        function checkAnswer(ans) {
            const res = document.getElementById('result');
            if(ans === 5) {
                res.innerHTML = '<span style="color:green">Jawaban Benar! Anda berhasil menyelesaikan quest.</span>';
            } else {
                res.innerHTML = '<span style="color:red">Jawaban Salah. Silakan coba lagi.</span>';
            }
        }
    </script>
</body>
</html>"""

    content_map = {
        "bacaan": {
            "judul": "Pengantar Aljabar Linear",
            "text": "## Apa itu Aljabar Linear?\n\nAljabar linear adalah cabang matematika yang mempelajari **vektor**, **matriks**, dan **transformasi linear**.\n\n### Contoh Penerapan\n\nAljabar linear digunakan dalam:\n- Grafis komputer\n- Machine learning\n- Fisika modern\n\n### Kesimpulan\n\nMemahami aljabar linear sangat penting dalam berbagai bidang ilmu.",
            "source": "Buku Matematika Kelas X",
            "image_path": None
        },
        "quiz_pg": {
            "soal": [
                {
                    "id": "pg-001",
                    "stimulus": "Perhatikan persamaan berikut: 2x + 3 = 7",
                    "image_path": None,
                    "soal": "Berapakah nilai x yang memenuhi persamaan tersebut?",
                    "pilihan": ["x = 1", "x = 2", "x = 3", "x = 4"],
                    "jawaban": 1,
                    "penjelasan": "2x + 3 = 7 → 2x = 4 → x = 2"
                },
                {
                    "id": "pg-002",
                    "stimulus": "Diketahui matriks A = [[1,2],[3,4]]",
                    "image_path": None,
                    "soal": "Berapakah determinan matriks A?",
                    "pilihan": ["-2", "2", "-10", "10"],
                    "jawaban": 0,
                    "penjelasan": "det(A) = (1×4) - (2×3) = 4 - 6 = -2"
                },
                {
                    "id": "pg-003",
                    "stimulus": "Sebuah vektor v = (3, 4)",
                    "image_path": None,
                    "soal": "Berapakah panjang (magnitude) vektor v?",
                    "pilihan": ["3", "4", "5", "7"],
                    "jawaban": 2,
                    "penjelasan": "|v| = √(3² + 4²) = √(9+16) = √25 = 5"
                }
            ]
        },
        "quiz_essay": {
            "pertanyaan": [
                {
                    "id": "essay-001",
                    "stimulus": "Dalam kehidupan sehari-hari, banyak masalah yang dapat diselesaikan menggunakan sistem persamaan linear.",
                    "image_path": None,
                    "soal": "Jelaskan pengertian sistem persamaan linear dan berikan contoh penerapannya dalam kehidupan nyata!",
                    "rubrik": "1. Menyebutkan definisi sistem persamaan linear (25 poin)\n2. Menjelaskan minimal 2 contoh penerapan (50 poin)\n3. Penjelasan logis dan runtut (25 poin)",
                    "penjelasan": "Sistem persamaan linear adalah kumpulan persamaan linear yang memiliki variabel yang sama. Contoh: menghitung harga barang, menentukan campuran larutan, dll."
                },
                {
                    "id": "essay-002",
                    "stimulus": "Matriks adalah salah satu konsep penting dalam aljabar linear.",
                    "image_path": None,
                    "soal": "Apa perbedaan antara matriks singular dan non-singular? Mengapa hal ini penting?",
                    "rubrik": "1. Definisi matriks singular (25 poin)\n2. Definisi matriks non-singular (25 poin)\n3. Penjelasan pentingnya perbedaan tersebut (50 poin)",
                    "penjelasan": "Matriks singular memiliki determinan = 0 dan tidak memiliki invers. Matriks non-singular memiliki determinan ≠ 0 dan memiliki invers."
                }
            ]
        },
        "flashcard": {
            "cards": [
                {
                    "depan": "Apa itu vektor?",
                    "belakang": "Vektor adalah besaran yang memiliki nilai (magnitude) dan arah. Contoh: kecepatan, gaya."
                },
                {
                    "depan": "Apa itu matriks identitas?",
                    "belakang": "Matriks identitas adalah matriks persegi dengan elemen diagonal utama bernilai 1 dan elemen lainnya 0."
                },
                {
                    "depan": "Apa itu determinan?",
                    "belakang": "Determinan adalah nilai skalar yang dihitung dari matriks persegi. Untuk matriks 2x2: det([[a,b],[c,d]]) = ad - bc."
                },
                {
                    "depan": "Apa itu transformasi linear?",
                    "belakang": "Transformasi linear adalah fungsi antara dua ruang vektor yang mempertahankan operasi penjumlahan vektor dan perkalian skalar."
                }
            ],
            "source": "Buku Matematika Kelas X"
        },
        "mindmap": {
            "nodes": [
                {
                    "id": "root",
                    "label": "Aljabar Linear",
                    "parent_id": None,
                    "penjelasan": "Cabang matematika yang mempelajari vektor, matriks, dan transformasi linear"
                },
                {
                    "id": "node-1",
                    "label": "Vektor",
                    "parent_id": "root",
                    "penjelasan": "Besaran yang memiliki nilai dan arah"
                },
                {
                    "id": "node-2",
                    "label": "Matriks",
                    "parent_id": "root",
                    "penjelasan": "Susunan bilangan dalam baris dan kolom"
                },
                {
                    "id": "node-3",
                    "label": "Transformasi Linear",
                    "parent_id": "root",
                    "penjelasan": "Fungsi yang mempertahankan operasi vektor"
                },
                {
                    "id": "node-1-1",
                    "label": "Operasi Vektor",
                    "parent_id": "node-1",
                    "penjelasan": "Penjumlahan, pengurangan, dan perkalian skalar"
                },
                {
                    "id": "node-1-2",
                    "label": "Magnitude",
                    "parent_id": "node-1",
                    "penjelasan": "Panjang vektor dihitung dengan rumus Pythagoras"
                },
                {
                    "id": "node-2-1",
                    "label": "Determinan",
                    "parent_id": "node-2",
                    "penjelasan": "Nilai skalar dari matriks persegi"
                },
                {
                    "id": "node-2-2",
                    "label": "Invers Matriks",
                    "parent_id": "node-2",
                    "penjelasan": "Matriks yang jika dikalikan matriks asal menghasilkan matriks identitas"
                }
            ]
        },
        "pretest": {
            "soal": [
                {
                    "id": "pretest_001",
                    "tingkat_kesulitan": "lots",
                    "image_path": None,
                    "jawaban": 1,
                    "stimulus": "Bayangkan kamu sedang belajar topik ini untuk pertama kali.",
                    "soal": "Apakah kamu mengenali konsep dasar dari topik ini?",
                    "pilihan": [
                        "Belum pernah mempelajari topik ini sama sekali",
                        "Pernah mendengar tapi belum memahami konsepnya",
                        "Sudah memahami sebagian konsep dasar",
                        "Sudah memahami dan bisa menerapkan konsepnya"
                    ]
                },
                {
                    "id": "pretest_002",
                    "tingkat_kesulitan": "lots",
                    "image_path": None,
                    "jawaban": 0,
                    "stimulus": "Perhatikan contoh-contoh berikut yang berkaitan dengan topik ini.",
                    "soal": "Manakah yang merupakan contoh paling sederhana dari topik ini?",
                    "pilihan": [
                        "Belum pernah mempelajari topik ini sama sekali",
                        "Pernah mendengar tapi belum memahami konsepnya",
                        "Sudah memahami sebagian konsep dasar",
                        "Sudah memahami dan bisa menerapkan konsepnya"
                    ]
                },
                {
                    "id": "pretest_003",
                    "tingkat_kesulitan": "lots",
                    "image_path": None,
                    "jawaban": 1,
                    "stimulus": "Seorang guru memperkenalkan topik ini kepada siswanya.",
                    "soal": "Seberapa jauh pemahamanmu sebelum pembelajaran dimulai?",
                    "pilihan": [
                        "Belum pernah mempelajari topik ini sama sekali",
                        "Pernah mendengar tapi belum memahami konsepnya",
                        "Sudah memahami sebagian konsep dasar",
                        "Sudah memahami dan bisa menerapkan konsepnya"
                    ]
                },
                {
                    "id": "pretest_004",
                    "tingkat_kesulitan": "mots",
                    "image_path": None,
                    "jawaban": 0,
                    "stimulus": "Seorang siswa menghadapi masalah yang membutuhkan pemahaman topik ini.",
                    "soal": "Bagaimana kamu menerapkan topik ini dalam situasi sehari-hari?",
                    "pilihan": [
                        "Belum pernah mempelajari topik ini sama sekali",
                        "Pernah mendengar tapi belum memahami konsepnya",
                        "Sudah memahami sebagian konsep dasar",
                        "Sudah memahami dan bisa menerapkan konsepnya"
                    ]
                },
                {
                    "id": "pretest_005",
                    "tingkat_kesulitan": "mots",
                    "image_path": None,
                    "jawaban": 1,
                    "stimulus": "Dalam kehidupan nyata, topik ini sering ditemukan dalam berbagai situasi.",
                    "soal": "Analisislah hubungan antara topik ini dengan konsep yang berkaitan!",
                    "pilihan": [
                        "Belum pernah mempelajari topik ini sama sekali",
                        "Pernah mendengar tapi belum memahami konsepnya",
                        "Sudah memahami sebagian konsep dasar",
                        "Sudah memahami dan bisa menerapkan konsepnya"
                    ]
                },
                {
                    "id": "pretest_006",
                    "tingkat_kesulitan": "mots",
                    "image_path": None,
                    "jawaban": 2,
                    "stimulus": "Terdapat beberapa pendekatan berbeda dalam memahami topik ini.",
                    "soal": "Pendekatan mana yang paling efektif untuk memahami topik ini?",
                    "pilihan": [
                        "Belum pernah mempelajari topik ini sama sekali",
                        "Pernah mendengar tapi belum memahami konsepnya",
                        "Sudah memahami sebagian konsep dasar",
                        "Sudah memahami dan bisa menerapkan konsepnya"
                    ]
                },
                {
                    "id": "pretest_007",
                    "tingkat_kesulitan": "mots",
                    "image_path": None,
                    "jawaban": 2,
                    "stimulus": "Sebuah permasalahan kompleks memerlukan pemahaman mendalam tentang topik ini.",
                    "soal": "Bagaimana kamu mengidentifikasi komponen utama dari topik ini?",
                    "pilihan": [
                        "Belum pernah mempelajari topik ini sama sekali",
                        "Pernah mendengar tapi belum memahami konsepnya",
                        "Sudah memahami sebagian konsep dasar",
                        "Sudah memahami dan bisa menerapkan konsepnya"
                    ]
                },
                {
                    "id": "pretest_008",
                    "tingkat_kesulitan": "hots",
                    "image_path": None,
                    "jawaban": 2,
                    "stimulus": "Seorang ahli diminta mengevaluasi solusi terbaik berkaitan dengan topik ini.",
                    "soal": "Evaluasi pendekatan terbaik untuk memecahkan masalah menggunakan topik ini!",
                    "pilihan": [
                        "Belum pernah mempelajari topik ini sama sekali",
                        "Pernah mendengar tapi belum memahami konsepnya",
                        "Sudah memahami sebagian konsep dasar",
                        "Sudah memahami dan bisa menerapkan konsepnya"
                    ]
                },
                {
                    "id": "pretest_009",
                    "tingkat_kesulitan": "hots",
                    "image_path": None,
                    "jawaban": 3,
                    "stimulus": "Dalam konteks akademik tingkat lanjut, topik ini memiliki peran kritis.",
                    "soal": "Sintesiskan pengetahuanmu untuk menghasilkan solusi inovatif dari topik ini!",
                    "pilihan": [
                        "Belum pernah mempelajari topik ini sama sekali",
                        "Pernah mendengar tapi belum memahami konsepnya",
                        "Sudah memahami sebagian konsep dasar",
                        "Sudah memahami dan bisa menerapkan konsepnya"
                    ]
                },
                {
                    "id": "pretest_010",
                    "tingkat_kesulitan": "hots",
                    "image_path": None,
                    "jawaban": 0,
                    "stimulus": "Sebuah studi kasus membutuhkan analisis mendalam tentang topik ini.",
                    "soal": "Bagaimana kamu merancang strategi terbaik menggunakan konsep topik ini?",
                    "pilihan": [
                        "Belum pernah mempelajari topik ini sama sekali",
                        "Pernah mendengar tapi belum memahami konsepnya",
                        "Sudah memahami sebagian konsep dasar",
                        "Sudah memahami dan bisa menerapkan konsepnya"
                    ]
                },
            ]
        },
        "game": {
            "data": {
                "game_id": f"game_{int(datetime.now(timezone.utc).timestamp() * 1000)}",
                "nama": "Quest: Persamaan Linear",
                "deskripsi": f"Game edukasi interaktif tentang Persamaan Linear — level {level}",
                "mapel_id": "mat",
                "elemen_id": "bil_aljabar",
                "elemen_label": "Bilangan dan Aljabar",
                "materi": "Persamaan Linear",
                "materi_id": "mat__persamaan_linear",
                "level": level,
                "status": "ready",
                "html_string": mock_game_html
            },
            "meta": None,
            "error": None
        }
    }

    return {
        "konten_id": str(uuid.uuid4()),
        "tipe": tipe,
        "level": level,
        "content": content_map.get(tipe, {}),
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }