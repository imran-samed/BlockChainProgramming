from cblock import CBlock, SomeClass

if __name__ == '__main__':
    root = CBlock("root", None)
    B1 = CBlock("B1", root)
    B2 = CBlock('B2', B1)
    B3 = CBlock(12345, B2)
    B4 = CBlock(SomeClass('B4'), B3)
    B5 = CBlock('B5', B4)

    for b in [B1, B2, B3, B4, B5]:
        if b.previous_block.compute_hash() == b.previous_hash:
            print("Success !, Hash is good")
        else:
            print("ERROR !, Hash is tampered.")

    B3.data = 787970
    if B4.previous_block.compute_hash() == B4.previous_hash:
        print("Success !, B4 Hash is good")
    else:
        print("ERROR !,B4  Hash is tampered.")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
