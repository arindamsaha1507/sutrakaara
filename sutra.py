"""Module for Sutras."""

from __future__ import annotations


# pylint: disable=non-ascii-name, invalid-name

import copy
import inspect

from varna import anunaasika_svara, vyanjana
from vinyaasa import get_vinyaasa, get_shabda

from utils import Prakriya, Khanda, KhandaType


def sutra_1_3_1(prakriya: Prakriya, dhaatu):
    """Return the Dhatus in the Prakriya that are Bhuvadis, Adis, etc."""

    stack = inspect.stack()
    if stack[1].function == "add_dhaatu":
        prakriya.add_to_prakriya([dhaatu], "भूवादयो धातवः १.३.१", "धातु-संज्ञा")

    return prakriya


def sutra_1_3_2(prakriya: Prakriya):
    """Return the Dhatus in the Prakriya that have an Upadesha with Janunasi and Anunasika."""

    varnas = []
    indices = []

    aupadeshika_khanda = [
        khanda for khanda in prakriya.vartamaana_sthiti if khanda.aupadeshika
    ]

    aupadeshika_khanda_index = [
        ii for ii, khanda in enumerate(prakriya.vartamaana_sthiti) if khanda.aupadeshika
    ]

    if not aupadeshika_khanda:
        return

    if len(aupadeshika_khanda) > 1:
        raise ValueError("Only one Aupadeshika Khanda is allowed")

    aupadeshika_khanda = aupadeshika_khanda[0]
    aupadeshika_khanda_index = aupadeshika_khanda_index[0]

    vinyaasa = get_vinyaasa(aupadeshika_khanda.roopa)
    print(vinyaasa)

    check = [varna in anunaasika_svara for varna in vinyaasa]

    if any(check):
        varnas.extend([vinyaasa[ii] for ii, jj in enumerate(check) if jj])
        indices.extend([ii for ii, jj in enumerate(check) if jj])

    for idx in indices.copy():
        if idx + 1 < len(vinyaasa) and vinyaasa[idx + 1] not in vyanjana:
            if vinyaasa[idx + 1] == "॒":
                aupadeshika_khanda.anudaatta_it = True
            else:
                aupadeshika_khanda.svarita_it = True

            indices.append(idx + 1)

    if varnas:
        varnas = [varna[0] for varna in varnas]
        aupadeshika_khanda.it.extend(varnas)
        prakriya.add_to_prakriya(
            prakriya.vartamaana_sthiti,
            "उपदेशे अजनुनासिकः इत् १.३.१",
            f"{'कार-'.join(varnas)}कार-इत्",
        )

        sutra_1_3_9(prakriya, aupadeshika_khanda, aupadeshika_khanda_index, indices)


def vartika_1_3_2(prakriya: Prakriya):
    """Return the Dhatus in the Prakriya that have an It with Anunaasika, R and I."""

    aupaadheshika_khanda = [
        khanda for khanda in prakriya.vartamaana_sthiti if khanda.aupadeshika
    ]

    aupaadheshika_khanda_index = [
        ii for ii, khanda in enumerate(prakriya.vartamaana_sthiti) if khanda.aupadeshika
    ]

    if not aupaadheshika_khanda:
        return

    aupaadheshika_khanda = aupaadheshika_khanda[0]

    if KhandaType.DHAATU not in aupaadheshika_khanda.typ:
        return

    vinyaasa = get_vinyaasa(aupaadheshika_khanda.roopa)

    if vinyaasa[-1] == "र्":
        indices = [len(vinyaasa) - 1]
        indices.append(len(vinyaasa) - 2)

        if vinyaasa[-2] != "इँ":
            indices.append(len(vinyaasa) - 3)
            if vinyaasa[-2] == "॒":
                aupaadheshika_khanda.anudaatta_it = True
            else:
                aupaadheshika_khanda.svarita_it = True

        aupaadheshika_khanda.it.extend(["इर्"])

        prakriya.add_to_prakriya(
            prakriya.vartamaana_sthiti,
            "इँर इत्संज्ञा वाच्या (वार्तिक)",
            "इर्-इत्",
        )

        sutra_1_3_9(prakriya, aupaadheshika_khanda, aupaadheshika_khanda_index[0], indices)


def sutra_1_3_3(prakriya: Prakriya):
    """Return the Dhatus in the Prakriya that have a Halantya."""

    aupaadheshika_khanda = [
        khanda for khanda in prakriya.vartamaana_sthiti if khanda.aupadeshika
    ]

    aupaadheshika_khanda_index = [
        ii for ii, khanda in enumerate(prakriya.vartamaana_sthiti) if khanda.aupadeshika
    ]

    if not aupaadheshika_khanda:
        return

    aupaadheshika_khanda = aupaadheshika_khanda[0]

    if "इर्" in aupaadheshika_khanda.it:
        return

    vinyaasa = get_vinyaasa(aupaadheshika_khanda.roopa)

    if vinyaasa[-1] in vyanjana:
        indices = [len(vinyaasa) - 1]
        aupaadheshika_khanda.it.extend([vinyaasa[-1]])

        prakriya.add_to_prakriya(
            prakriya.vartamaana_sthiti,
            "हलन्त्यम् १.३.३",
            f"{vinyaasa[-1][0]}कार इत्",
        )

        sutra_1_3_9(prakriya, aupaadheshika_khanda, aupaadheshika_khanda_index[0], indices)


def sutra_1_3_4(prakriya: Prakriya):
    """Return the Dhatus in the Prakriya that have a Halantya."""

    aupaadheshika_khanda = [
        khanda for khanda in prakriya.vartamaana_sthiti if khanda.aupadeshika
    ]

    aupaadheshika_khanda_index = [
        ii for ii, khanda in enumerate(prakriya.vartamaana_sthiti) if khanda.aupadeshika
    ]

    if not aupaadheshika_khanda:
        return

    aupaadheshika_khanda = aupaadheshika_khanda[0]

    vinyaasa = get_vinyaasa(aupaadheshika_khanda.roopa)

    if get_shabda(vinyaasa[:2]) in ["ञि", "टु", "डु"]:
        indices = [0, 1]
        aupaadheshika_khanda.it.extend([get_shabda(vinyaasa[:2])])

        if vinyaasa[2] not in vyanjana and vinyaasa[2] not in anunaasika_svara:
            indices.append(2)
            if vinyaasa[2] == "॒":
                aupaadheshika_khanda.anudaatta_it = True
            else:
                aupaadheshika_khanda.svarita_it = True

        prakriya.add_to_prakriya(
            prakriya.vartamaana_sthiti,
            "आदिर्ञिटुडवः १.३.४",
            f"{get_shabda(vinyaasa[:2])} इत्",
        )

        sutra_1_3_9(prakriya, aupaadheshika_khanda, aupaadheshika_khanda_index[0], indices)


def sutra_1_3_9(prakriya: Prakriya, khanda: Khanda, khanda_index: int, indices: list[int]):
    """Delete the varnas from the Aupadeshika Khanda."""

    print(indices)

    vinyaasa = get_vinyaasa(khanda.roopa)

    for index in sorted(indices, reverse=True):
        del vinyaasa[index]

    khanda.roopa = get_shabda(vinyaasa)

    sthiti = copy.deepcopy(prakriya.vartamaana_sthiti)
    sthiti[khanda_index] = khanda

    prakriya.add_to_prakriya(
        sthiti,
        "तस्य लोपः १.३.९",
        "इत्-लोपः",
    )
