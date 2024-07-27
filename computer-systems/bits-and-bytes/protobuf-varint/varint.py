def encode(n: int) -> bytes:
    # 1. Group into bytes, leaving room for the continuation bits
    a = 0
    i = 0
    while n:
        a += (n & 0b01111111) << i * 8
        n >>= 7
        i += 1

    # 2. Convert to little-endian order
    bytes = bytearray(a.to_bytes(num_bytes(a), "little"))

    # 2. Add continuation bit
    for i in range(len(bytes) - 1):
        bytes[i] |= 0b10000000

    return bytes


def decode(bytes: bytes) -> int:
    # Q: how can I drop a bit??
    # Idea: Can I shift instead?
    concat = 0
    for i, byte in enumerate(bytes):
        # 1. Drop the MSB/continuation byte
        msb = byte & 0b10000000  # Read continuation bit
        byte &= 0b01111111  # Unset the continuation bit

        # 2. Convert to big-endian order
        # 3. Concatenate and interpret as an integer
        concat += byte << (i * 7)

        # See if we need to keep going
        if not msb:
            break

    n = concat.to_bytes(num_bytes(concat))
    return int.from_bytes(n)


def num_bytes(n: int) -> int:
    # Initial version: return math.ceil(math.floor(math.log2(n) + 1) / 8)
    return (n.bit_length() + 7) // 8


def format_bytes(bytes: bytes) -> str:
    return " ".join(format(byte, "08b") for byte in bytes)


def print_binary(n: int):
    print(format(n, "08b"))


def test(got, want):
    print("got: ", got)
    print("want:", want)


if __name__ == "__main__":
    print("Encode tests:")
    test(format_bytes(encode(150)), "10010110 00000001")
    print()

    print("Decode tests:")
    test(decode(bytes([0b10010110, 0b00000001])), 150)
    test(decode(bytes.fromhex("9601")), 150)
    test(decode(bytes([0b00000001])), 1)
    test(decode((1).to_bytes()), 1)
    print()

    print("Property tests:")
    for i in range(1000000):
        assert decode(encode(i)) == i
    max = 2**64 - 1
    assert decode(encode(max)) == max
    print("ok")
