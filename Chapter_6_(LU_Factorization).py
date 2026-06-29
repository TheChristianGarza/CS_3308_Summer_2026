{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPx7O9uLBEyk70sQnTd7u0r",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/TheChristianGarza/CS_3308_Summer_2026/blob/main/Chapter_6_(LU_Factorization).py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "id": "hIyStQqraM1n",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 408
        },
        "outputId": "f6d7a6c5-427e-45dd-8a2a-fa7a817effa9"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter matrix size n (n×n matrix):\n",
            "4\n",
            "Enter the 4×4 matrix row by row, values separated by spaces.\n",
            "You may use integers, decimals, fractions, sqrt(), pi, e, etc.\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_6921/779999566.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m    102\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    103\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"__main__\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 104\u001b[0;31m     \u001b[0mmain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/tmp/ipykernel_6921/779999566.py\u001b[0m in \u001b[0;36mmain\u001b[0;34m()\u001b[0m\n\u001b[1;32m     93\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mmain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     94\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 95\u001b[0;31m     \u001b[0mA\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mget_user_matrix\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     96\u001b[0m     \u001b[0mprint_matrix\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mA\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"Matrix\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     97\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/tmp/ipykernel_6921/779999566.py\u001b[0m in \u001b[0;36mget_user_matrix\u001b[0;34m()\u001b[0m\n\u001b[1;32m     57\u001b[0m     \u001b[0mA\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     58\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 59\u001b[0;31m         \u001b[0mrow_input\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf\"Row {i+1}: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     60\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow_input\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mn\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     61\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Row length does not match matrix size.\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m   1175\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1176\u001b[0m             )\n\u001b[0;32m-> 1177\u001b[0;31m         return self._input_request(\n\u001b[0m\u001b[1;32m   1178\u001b[0m             \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprompt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1179\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"shell\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m   1217\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1218\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1219\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1220\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1221\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ],
      "source": [
        "\"\"\"\n",
        "Chapter 6 (LU Factorization)\n",
        "Christian Garza\n",
        "Esmeralda Nuno Cortrez\n",
        "June 28th, 2026\n",
        "\"\"\"\n",
        "\n",
        "from fractions import Fraction\n",
        "import math\n",
        "\n",
        "# Allowed names for safe eval\n",
        "allowed = {\n",
        "    \"Fraction\": Fraction,\n",
        "    \"sqrt\": math.sqrt,\n",
        "    \"pi\": math.pi,\n",
        "    \"e\": math.e\n",
        "}\n",
        "\n",
        "#This is to make sure the outputs for our solution are easy to read\n",
        "def parse_value(expr):\n",
        "    expr = expr.strip()\n",
        "\n",
        "    #integers\n",
        "    if expr.isdigit() or (expr.startswith('-') and expr[1:].isdigit()):\n",
        "        return Fraction(int(expr))\n",
        "\n",
        "    #decimals\n",
        "    try:\n",
        "        if \".\" in expr and all(c.isdigit() or c in \".-\" for c in expr):\n",
        "            return float(expr)\n",
        "    except:\n",
        "        pass\n",
        "\n",
        "    #fractions\n",
        "    if \"/\" in expr and all(x not in expr for x in [\"sqrt\", \"pi\", \"e\"]):\n",
        "        try:\n",
        "            return Fraction(expr)\n",
        "        except:\n",
        "            pass\n",
        "\n",
        "    #Expressions (sqrt, pi, e)\n",
        "    try:\n",
        "        return eval(expr, {\"__builtins__\": None}, allowed)\n",
        "    except Exception:\n",
        "        raise ValueError(f\"Invalid expression: {expr}\")\n",
        "\n",
        "#This is to stop whole numbers being printed out with decimals\n",
        "def to_decimal(x):\n",
        "    val = float(x)\n",
        "    rounded = round(val, 6)\n",
        "\n",
        "    if abs(rounded - int(rounded)) < 1e-6:\n",
        "        return str(int(rounded))\n",
        "    return f\"{rounded:.6f}\".rstrip('0').rstrip('.')\n",
        "\n",
        "\n",
        "def get_user_matrix():\n",
        "    print(\"Enter matrix size n (n×n matrix):\")\n",
        "    n = int(input(\"\"))\n",
        "\n",
        "    print(f\"Enter the {n}×{n} matrix row by row, values separated by spaces.\")\n",
        "    print(\"You may use integers, decimals, fractions, sqrt(), pi, e, etc.\")\n",
        "\n",
        "    A = []\n",
        "    for i in range(n):\n",
        "        row_input = input(f\"Row {i+1}: \").split()\n",
        "        if len(row_input) != n:\n",
        "            raise ValueError(\"Row length does not match matrix size.\")\n",
        "        row = [parse_value(x) for x in row_input]\n",
        "        A.append(row)\n",
        "\n",
        "    return A\n",
        "\n",
        "\n",
        "def lu_factorization(A):\n",
        "    n = len(A)\n",
        "    L = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]\n",
        "    U = [[Fraction(0) for _ in range(n)] for _ in range(n)]\n",
        "\n",
        "    for i in range(n):\n",
        "        # Compute U row\n",
        "        for j in range(i, n):\n",
        "            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))\n",
        "\n",
        "        # Compute L column\n",
        "        for j in range(i+1, n):\n",
        "            if U[i][i] == 0:\n",
        "                raise ValueError(\"Zero pivot encountered! Cannot compute LU without pivoting.\")\n",
        "            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]\n",
        "\n",
        "    return L, U\n",
        "\n",
        "\n",
        "def print_matrix(M, name):\n",
        "    print(f\"\\n{name}:\")\n",
        "    for row in M:\n",
        "        print(\"  \".join(to_decimal(x) for x in row))\n",
        "\n",
        "\n",
        "def main():\n",
        "\n",
        "    A = get_user_matrix()\n",
        "    print_matrix(A, \"Matrix\")\n",
        "\n",
        "    L, U = lu_factorization(A)\n",
        "    print_matrix(L, \"L Matrix\")\n",
        "    print_matrix(U, \"U Matrix\")\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    }
  ]
}