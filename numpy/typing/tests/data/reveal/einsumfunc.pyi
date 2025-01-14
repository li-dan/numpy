from typing import Any
import numpy as np
import numpy.typing as npt

AR_LIKE_b: list[bool]
AR_LIKE_u: list[np.uint32]
AR_LIKE_i: list[int]
AR_LIKE_f: list[float]
AR_LIKE_c: list[complex]
AR_LIKE_U: list[str]
AR_o: npt.NDArray[np.object_]

OUT_f: npt.NDArray[np.float64]

reveal_type(np.einsum("i,i->i", AR_LIKE_b, AR_LIKE_b))  # E: Any
reveal_type(np.einsum("i,i->i", AR_o, AR_o))  # E: Any
reveal_type(np.einsum("i,i->i", AR_LIKE_u, AR_LIKE_u))  # E: Any
reveal_type(np.einsum("i,i->i", AR_LIKE_i, AR_LIKE_i))  # E: Any
reveal_type(np.einsum("i,i->i", AR_LIKE_f, AR_LIKE_f))  # E: Any
reveal_type(np.einsum("i,i->i", AR_LIKE_c, AR_LIKE_c))  # E: Any
reveal_type(np.einsum("i,i->i", AR_LIKE_b, AR_LIKE_i))  # E: Any
reveal_type(np.einsum("i,i,i,i->i", AR_LIKE_b, AR_LIKE_u, AR_LIKE_i, AR_LIKE_c))  # E: Any

reveal_type(np.einsum("i,i->i", AR_LIKE_c, AR_LIKE_c, out=OUT_f))  # E: ndarray[Any, dtype[{float64}]
reveal_type(np.einsum("i,i->i", AR_LIKE_U, AR_LIKE_U, dtype=bool, casting="unsafe", out=OUT_f))  # E: ndarray[Any, dtype[{float64}]
reveal_type(np.einsum("i,i->i", AR_LIKE_f, AR_LIKE_f, dtype="c16"))  # E: Any
reveal_type(np.einsum("i,i->i", AR_LIKE_U, AR_LIKE_U, dtype=bool, casting="unsafe"))  # E: Any

reveal_type(np.einsum_path("i,i->i", AR_LIKE_b, AR_LIKE_b))  # E: tuple[builtins.list[Any], builtins.str]
reveal_type(np.einsum_path("i,i->i", AR_LIKE_u, AR_LIKE_u))  # E: tuple[builtins.list[Any], builtins.str]
reveal_type(np.einsum_path("i,i->i", AR_LIKE_i, AR_LIKE_i))  # E: tuple[builtins.list[Any], builtins.str]
reveal_type(np.einsum_path("i,i->i", AR_LIKE_f, AR_LIKE_f))  # E: tuple[builtins.list[Any], builtins.str]
reveal_type(np.einsum_path("i,i->i", AR_LIKE_c, AR_LIKE_c))  # E: tuple[builtins.list[Any], builtins.str]
reveal_type(np.einsum_path("i,i->i", AR_LIKE_b, AR_LIKE_i))  # E: tuple[builtins.list[Any], builtins.str]
reveal_type(np.einsum_path("i,i,i,i->i", AR_LIKE_b, AR_LIKE_u, AR_LIKE_i, AR_LIKE_c))  # E: tuple[builtins.list[Any], builtins.str]

reveal_type(np.einsum([[1, 1], [1, 1]], AR_LIKE_i, AR_LIKE_i))  # E: Any
reveal_type(np.einsum_path([[1, 1], [1, 1]], AR_LIKE_i, AR_LIKE_i))  # E: tuple[builtins.list[Any], builtins.str]
