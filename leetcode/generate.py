
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void generate(char **result, char *current,
              int open, int close, int n, int *count) {

    if (open == n && close == n) {
        current[2 * n] = '\0';
        result[*count] = malloc(2 * n + 1);
        strcpy(result[*count], current);
        (*count)++;
        return;
    }

    if (open < n) {
        current[open + close] = '(';
        generate(result, current, open + 1, close, n, count);
    }

    if (close < open) {
        current[open + close] = ')';
        generate(result, current, open, close + 1, n, count);
    }
}

char** generateParenthesis(int n, int* returnSize) {

    int total = 1;
    for (int i = 0; i < n; i++) {
        total = total * 2;
    }

    char **result = malloc(total * sizeof(char *));
    char *current = malloc((2 * n + 1) * sizeof(char));

    *returnSize = 0;

    generate(result, current, 0, 0, n, returnSize);

    free(current);
    return result;
}
