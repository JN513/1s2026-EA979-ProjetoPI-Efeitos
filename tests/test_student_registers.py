from utils import assert_valid_ra

from unicamp_effects.registry import get_all_effects


def test_student_registers():
    effects = get_all_effects()

    assert len(effects) >= 3

    ra = next(iter(effects)).split("_")[0]
    assert_valid_ra(ra)

    for name in effects:
        assert name.split("_")[0] == ra
