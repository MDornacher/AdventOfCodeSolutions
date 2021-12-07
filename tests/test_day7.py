import numpy as np
import pytest

from aocs.day7 import solve_a, solve_b, main, create_fuel_template

TEST_INPUT = "16,1,2,0,4,2,7,1,2,14"


@pytest.mark.parametrize(
    "width, template",
    [
        (0, np.array([0])),
        (1, np.array([1, 0, 1])),
        (2, np.array([2, 1, 0, 1, 2])),
    ]
)
def test_create_fuel_template_linear(width, template):
    mode = "linear"
    np.testing.assert_array_equal(
        create_fuel_template(mode, width),
        template
    )


@pytest.mark.parametrize(
    "width, template",
    [
        (0, np.array([0])),
        (3, np.array([6, 3, 1, 0, 1, 3, 6])),
    ]
)
def test_create_fuel_template_triangle(width, template):
    mode = "triangle"
    np.testing.assert_array_equal(
        create_fuel_template(mode, width),
        template
    )


def test_solve_a_with_example():
    assert solve_a(TEST_INPUT) == 37


def test_solve_b_with_example():
    assert solve_b(TEST_INPUT) == 168


def test_main():
    main()
