class Figure:
    def __init__(self, figure_type, sides):
        self.type = figure_type
        self.sides = sides


def test_app_triangle():
    """Test if we create triangle figure."""
    fig = "трикутник"
    triangle = Figure(fig, 3)  # Трикутник має 3 сторони
    assert triangle.type == fig, f"Фігура має бути {fig}"
    assert triangle.sides == 3, "Кількість сторін має бути 3"
