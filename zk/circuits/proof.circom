pragma circom 2.0.0;

template HashCheck() {
    signal input expected;
    signal input actual;

    signal output isValid;

    isValid <== 1 - (expected - actual)*(expected - actual);
}

component main = HashCheck();
