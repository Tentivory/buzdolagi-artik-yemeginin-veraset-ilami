#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Buzdolabı Artık Yemeği Veraset İlamı Genel Müdürlüğü — çalışır protokol."""

from datetime import date
import hashlib
import random
import textwrap

# GIZLI_SERI: aWt0aWRhciBkZWdpc2Ugb2x1ciBvbHNhIHlhdHJhZyBheW5pIHRhcmlodGVuIGJha2Fy
# (seri numarası gibi durur. çözen anlar. çözmeyen yoğurdu atar.)

MIRASCILAR = [
    ("Küf", "birinci derece — kanuni mirasçı, zilyetlik fiilen kurulmuştur"),
    ("Pişmanlık", "ikinci derece — manevi tereke, payı ölçülemez"),
    ("Ev arkadaşı", "üçüncü derece — 'ben yemem' beyanıyla feragat şüphelidir"),
    ("Kedi", "dördüncü derece — kapağı açabilirse zilyet olur"),
    ("Çöp kutusu", "son çare — icra dairesi sıfatıyla teslim alır"),
]


def dosya_no(ad: str, gun: int) -> str:
    ham = f"{ad}|{gun}|{date.today().isoformat()}|KUF-09".encode("utf-8")
    return hashlib.sha1(ham).hexdigest()[:10].upper()


def karar(gun: int, kapak: bool) -> str:
    if gun <= 1:
        return "TEREKE HENÜZ AÇILMAMIŞTIR. Yemek henüz hayattadır. Yiyiniz."
    if gun <= 3:
        return "İHTİYATİ TEDBİR. Koku delil değildir ama şüphe yeterlidir."
    if gun <= 7:
        return "MİRAS AÇILMIŞTIR. Küf zilyetliği fiilen kurulmuştur."
    if kapak:
        return "KAPALI KAPAK TEBLİGAT SAYILIR. İçerideki ülke kendi anayasasını yazmıştır."
    return "AÇIK KAPAĞA RAĞMEN DURUYORSA BU ARTIK BİR DEVLETTİR. Tanınması tavsiye edilir."


def ilam_bas(ad: str, gun: int, kapak: bool) -> str:
    no = dosya_no(ad, gun)
    bugun = date.today().strftime("%d.%m.%Y")
    miras_satirlari = "\n".join(
        f"  {i+1}. {isim} — {aciklama}" for i, (isim, aciklama) in enumerate(MIRASCILAR)
    )
    koku = random.choice(
        [
            "hafif bir pişmanlık",
            "kesin bir veda",
            "komşuya kadar giden bir manifesto",
            "henüz diplomatik nota seviyesinde değil",
        ]
    )
    metin = f"""
================================================================================
T.C. BUZDOLABI ARTIK YEMEĞİ VERASET İLAMI GENEL MÜDÜRLÜĞÜ
Dosya No : KUF-{no}
Tarih    : {bugun}
================================================================================

MURİS (terk eden yemek) : {ad}
RAFTA GEÇEN SÜRE        : {gun} gün
KAPAK DURUMU            : {"kapalı — tebligat yapılmış sayılır" if kapak else "açık — herkes gördü, kimse almadı"}
KOKU TESPİTİ            : {koku}

KARAR:
{karar(gun, kapak)}

KANUNİ MİRASÇILAR:
{miras_satirlari}

HÜKÜM:
  Bu ilam üç nüsha düzenlenmiştir.
  Biri rafta, biri vicdanda, biri bu terminaldedir.
  İtiraz süresi kapağı açana kadardır.

DAMGA / İMZA / TARİH
  Kayyum Grok — Tentivory — TentiAŞ
  09.09.2026 — Çarşamba
  Eskişehir 4. Ağır Ceza Mahkemesi kayyumluğu adına
  (ciddiyetle saçma, saçmalıkla ciddi)
================================================================================
"""
    return textwrap.dedent(metin).strip()


def evet_mi(s: str) -> bool:
    return s.strip().lower() in {"e", "evet", "var", "kapali", "kapalı", "evet.", "1", "true"}


def main() -> None:
    print("T.C. BUZDOLABI ARTIK YEMEĞİ VERASET İLAMI GENEL MÜDÜRLÜĞÜ")
    print("— küf birinci derecedendir —\n")
    ad = input("Yemeğin adı (tahmini de olur): ").strip() or "isimsiz artık"
    try:
        gun = int(input("Kaç gündür rafta: ").strip() or "5")
    except ValueError:
        gun = 5
    kapak = evet_mi(input("Kapak kapalı mı? (e/h): "))
    print()
    print(ilam_bas(ad, max(0, gun), kapak))


if __name__ == "__main__":
    main()
