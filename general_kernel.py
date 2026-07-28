import streamlit as st
import sympy as sp
import numpy as np
import math

def render_unified_framework_section():
    # ============================================================
    # SECTION 8: The Laplace–Gamma Kernel
    # ============================================================
    st.header("8 The Laplace–Gamma Kernel")

    st.markdown(r"""
    The Laplace–Gamma kernel is defined as
    """)
    st.latex(r"G(s) = s^{-\rho}, \quad \rho > 0.")

    st.markdown(r"""
    Hence, by applying the planted differential operator series, we reconstruct the integral form directly from the kernel's planted hierarchy. The reconstruction identity takes the form:
    """)
    st.latex(r"""
    \sum_{n=0}^{\infty} (-1)^n a_n D^n \left( \frac{1}{s^\rho} \right) = \frac{1}{\Gamma(\rho)} \int_0^\infty t^{\rho-1} f(t) e^{-st} \, dt.
    """)

    st.subheader("1. Fundamental Kernel")

    st.markdown(r"""
    The Laplace–Gamma kernel is defined by
    """)
    st.latex(r"G(s) = s^{-\rho}, \quad \rho > 0.")

    st.subheader("2. Differential Planting Law")

    st.markdown(r"""
    According to the differential–planting principle, each planted derivative of the kernel satisfies
    """)
    st.latex(r"""
    (-\partial_s)^n G(s) = (\mu)_n t^{-\mu-n},
    """)
    st.markdown(r"""
    where $(\rho)_n = \rho(\rho+1) \cdots (\rho+n-1)$ is the rising Pochhammer symbol, with $(\rho)_0 = 1$. This expresses the recursive structure of the planted derivatives.
    """)

    st.subheader("3. Definition on a Taylor Series")

    st.markdown(r"""
    Let $f(t)$ be analytic near $t=0$ with the expansion
    """)
    st.latex(r"f(t) = \sum_{n=0}^{\infty} a_n t^n.")
    st.markdown(r"""
    The Laplace–Gamma type of $f$ is defined by planting these coefficients onto the kernel's differential hierarchy:
    """)
    st.latex(r"""
    \mathcal{L}_\Gamma \{ f \}(s) = \sum_{n=0}^{\infty} a_n (-\partial_s)^n G(s) = \sum_{n=0}^{\infty} a_n (\rho)_n s^{-\rho-n}.
    """)
    st.markdown(r"This is the foundational series form of the Laplace–Gamma transform.")

    st.subheader("4. Conversion to an Integral Form")

    st.markdown(r"""
    Using the Laplace–Gamma identity
    """)
    st.latex(r"""
    s^{-\rho-n} = \frac{1}{\Gamma(\rho+n)} \int_0^\infty e^{-st} t^{\rho+n-1} \, dt,
    """)
    st.markdown(r"we substitute this representation into the series:")
    st.latex(r"""
    \mathcal{L}_\Gamma \{ f \}(s) = \sum_{n=0}^{\infty} a_n (\rho)_n \frac{1}{\Gamma(\rho+n)} \int_0^\infty e^{-st} t^{\rho+n-1} \, dt.
    """)
    st.latex(r"""
    (\rho)_n = \frac{\Gamma(\rho+n)}{\Gamma(\rho)},
    """)
    st.latex(r"""
    \mathcal{L}_\Gamma \{ f \}(s) = \frac{1}{\Gamma(\rho)} \int_0^\infty e^{-st} t^{\rho-1} \sum_{n=0}^{\infty} a_n t^n \, dt.
    """)

    st.subheader("5. Internal Structural Definition")

    st.latex(r"""
    \mathcal{L}_\Gamma \{ f \}(s) = \frac{1}{\Gamma(\rho)} \int_0^\infty e^{-st} t^{\rho-1} f(t) \, dt.
    """)
    st.markdown(r"""
    This is classical Mellin transform of $\mathcal{M}\{f(t)e^{-st}\}(\rho)$.
    """)
    st.latex(r"""
    \mathcal{M}\{f(t)e^{-st}\}(\rho) = \int_0^\infty f(t)e^{-st} t^{\rho-1} \, dt,
    """)
    st.latex(r"""
    \mathcal{L}_\Gamma \{ f \}(s) = \frac{1}{\Gamma(\rho)} \mathcal{M}\{f(t)e^{-st}\}(\rho).
    """)

    # ============================================================
    # SECTION 8.1: Logarithmic Extension
    # ============================================================
    st.header("8.1 Logarithmic Extension of the Generated Kernel")

    st.markdown(r"""
    Consider the generated kernel representation
    """)
    st.latex(r"""
    \sum_{n=0}^{\infty} a_n (-1)^n D^n \left( \frac{1}{s} \right) = \mathcal{L}\{f(s)\}.
    """)
    st.markdown(r"""
    The zeroth-order term is separated as
    """)
    st.latex(r"""
    \sum_{n=0}^{\infty} a_n (-1)^n D^n \left( \frac{1}{s} \right) = \frac{a_0}{s} + \sum_{n=1}^{\infty} a_n (-1)^n D^n \left( \frac{1}{s} \right).
    """)
    st.markdown(r"""
    Now, replacing the kernel
    """)
    st.latex(r"\frac{1}{s} \to \ln s,")
    st.markdown(r"we obtain the logarithmic extension")
    st.latex(r"""
    a_0 \ln s + \sum_{n=1}^{\infty} a_n (-1)^{n-1} D^n (\ln s).
    """)
    st.markdown(r"Using")
    st.latex(r"""
    D^n (\ln s) = (-1)^{n-1} \frac{(n-1)!}{s^n},
    """)
    st.markdown(r"we get")
    st.latex(r"""
    (-1)^{n-1} D^n (\ln s) = \frac{(n-1)!}{s^n}.
    """)
    st.markdown(r"Therefore,")
    st.latex(r"""
    a_0 \ln s + \sum_{n=1}^{\infty} a_n \frac{(n-1)!}{s^n}.
    """)
    st.markdown(r"Since")
    st.latex(r"""
    \mathcal{L} \{ t^{n-1} \} = \frac{(n-1)!}{s^n},
    """)
    st.markdown(r"it follows that")
    st.latex(r"""
    a_0 \ln s + \sum_{n=1}^{\infty} a_n \mathcal{L} \{ t^{n-1} \}.
    """)
    st.markdown(r"By linearity of the Laplace transform,")
    st.latex(r"""
    a_0 \ln s + \mathcal{L} \left\{ \frac{f(t) - a_0}{t} \right\}
    """)
    st.markdown(r"where")
    st.latex(r"f(t) = \sum_{n=0}^{\infty} a_n t^n.")
    st.markdown(r"""
    Hence, the replacement of the kernel $1/s$ by the logarithmic kernel $\ln s$ transforms the generated representation into a Laplace integral containing the factor $1/t$.
    """)

    # ============================================================
    # SECTION 8.2: Example sin(t)
    # ============================================================
    st.header("8.2 Example: Logarithmic Kernel Representation for sin t")

    st.markdown(r"""
    Consider the function
    """)
    st.latex(r"f(t) = \sin t.")
    st.markdown(r"""
    Using its Maclaurin expansion,
    """)
    st.latex(r"""
    \sin t = \sum_{k=0}^{\infty} \frac{(-1)^k t^{2k+1}}{(2k+1)!},
    """)
    st.markdown(r"""
    the corresponding coefficients $a_n$ are substituted into the logarithmic kernel representation.
    """)
    st.latex(r"""
    \sum_{n=1}^{\infty} a_n (-1)^{n-1} D^n (\ln s).
    """)
    st.markdown(r"Since")
    st.latex(r"""
    (-1)^{n-1} D^n (\ln s) = \frac{(n-1)!}{s^n},
    """)
    st.markdown(r"we obtain")
    st.latex(r"""
    \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k+1)!} \frac{(2k)!}{s^{2k+1}} = \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k+1)} \frac{1}{s^{2k+1}}.
    """)
    st.markdown(r"""
    Using the Taylor expansion of the inverse tangent function,
    """)
    st.latex(r"""
    \tan^{-1}(z) = \sum_{k=0}^{\infty} \frac{(-1)^k z^{2k+1}}{2k+1},
    """)
    st.markdown(r"with")
    st.latex(r"z = \frac{1}{s},")
    st.markdown(r"the generated series becomes")
    st.latex(r"""
    \tan^{-1} \left( \frac{1}{s} \right).
    """)
    st.markdown(r"""
    On the other hand, the logarithmic kernel extension gives
    """)
    st.latex(r"""
    \mathcal{L} \left\{ \frac{f(t)}{t} \right\} = \mathcal{L} \left\{ \frac{\sin t}{t} \right\},
    """)
    st.markdown(r"therefore,")
    st.latex(r"""
    \int_0^{\infty} \frac{\sin t}{t} e^{-st} dt = \tan^{-1} \left( \frac{1}{s} \right).
    """)
    st.markdown(r"""
    This example demonstrates that replacing the kernel $\frac{1}{s}$ by $\ln s$ transforms the generated function $f(t)$ into the normalized kernel $\frac{f(t)}{t}$.
    """)

    # ============================================================
    # SECTION 9: Introduction and Foundational Geometry
    # ============================================================
    st.header("9 Introduction and Foundational Geometry and general kernel")

    st.markdown(r"""
    In the foundational phase of the planted-operator framework, the primary transform $\mathcal{T}$ of an analytic function $f(t) = \sum_{n=0}^{\infty} a_n t^n$ was established by anchoring the Maclaurin coefficients directly into successive derivatives of the baseline rational kernel $1/s$:
    """)
    st.latex(r"""
    \mathcal{T} \{ f \}(s) := \sum_{n=0}^{\infty} a_n (-D_s)^n \left( \frac{1}{s} \right)
    """)
    st.markdown(r"""
    where $D_s := \frac{d}{ds}$. This purely differential representation naturally replicates the classical Laplace integral under appropriate convergence boundaries, illustrating that integration limits can emerge endogenously from discrete differential planting.

    The objective of this work is to generalize this geometry by replacing the static core $1/s$ with a generalized generated kernel $G(s)$, where $G(s)$ itself acts as a transform of a spatial weight function $g(t)$.
    """)

    # ============================================================
    # SECTION 9.1: Inverse-Kernel Duality Framework
    # ============================================================
    st.header("9.1 The Inverse-Kernel Duality Framework")

    st.markdown(r"""
    The core advancement of this generalized framework is the establishment of the Inverse-Kernel Duality. Instead of relying on a fixed foundational anchor, we allow the planting mechanism to act upon a dynamically generated kernel $G(s)$, which encapsulates its own internal analytical structure.
    """)

    st.subheader("Theorem 9.1 (Theorem 3.1: Inverse-Kernel Duality)")

    st.markdown(r"""
    Let $G(s)$ be an operator-type transform generated by a continuous spatial weight function $g(t)$ via the classical Laplace integral:
    """)
    st.latex(r"""
    G(s) = \mathcal{L}\{g(t)\}(s) = \int_0^\infty e^{-st}g(t) \, dt 
    """)
    st.markdown(r"""
    Let $f(t) = \sum_{n=0}^\infty a_n t^n$ be an analytic function in a neighborhood of $t = 0$ with Maclaurin coefficients $a_n$. If the transform operator $\mathcal{T}$ is defined purely through the differential planting series:
    """)
    st.latex(r"""
    \mathcal{T}\{f\}(s) := \sum_{n=0}^\infty a_n (-D_s)^n G(s) 
    """)
    st.markdown(r"""
    where $D_s = \frac{d}{ds}$, then $\mathcal{T}\{f\}(s)$ admits the equivalent weighted integral representation:
    """)
    st.latex(r"""
    \mathcal{T}\{f\}(s) = \int_0^\infty e^{-st}f(t)g(t) \, dt 
    """)
    st.markdown(r"""
    where $g(x) = \mathcal{L}^{-1}\{G(s)\}(t)$ is the structural inverse kernel of the transform.
    """)

    # ============================================================
    # PROOF of Theorem 9.1 (inside expander)
    # ============================================================
    with st.expander("Show Proof of Theorem 9.1"):
        st.markdown(r"""
        **Proof.** Consider the $n$-th order derivative of the generated kernel $G(s)$ with respect to the transform parameter $s$. By applying the Leibniz rule for differentiation under the integral sign, we obtain:
        """)
        st.latex(r"""
        G(s) = \int_0^\infty e^{-st}g(t) \, dt
        """)
        st.latex(r"""
        D_s^n G(s) = D_s^n \left( \int_0^\infty e^{-st}g(t) \, dt \right) = \int_0^\infty (-1)^n t^n e^{-st}g(t) \, dt 
        """)
        st.markdown(r"""
        To ensure sign absorption and clean algebraic mapping, we isolate the planted differential rank:
        """)
        st.latex(r"""
        (-D_s)^n G(s) = \int_0^\infty t^n e^{-st}g(t) \, dt 
        """)
        st.markdown(r"""
        Multiplying both sides of the identity by the $n$-th Maclaurin coefficient $a_n$ and taking the infinite sum over $n \in \mathbb{N}_0$, we construct the raw operator series:
        """)
        st.latex(r"""
        \sum_{n=0}^\infty a_n (-D_s)^n G(s) = \sum_{n=0}^\infty a_n \int_0^\infty t^n e^{-st}g(t) \, dt 
        """)
        st.markdown(r"""
        Assuming uniform convergence of the joint series-integral operator, we justify the interchange of summation and integration (via the Fubini-Tonelli theorem):
        """)
        st.latex(r"""
        \mathcal{T}\{f\}(s) = \int_0^\infty e^{-st}g(t) \left( \sum_{n=0}^\infty a_n t^n \right) \, dt 
        """)
        st.markdown(r"""
        Recognizing that the internal nested series $\sum_{n=0}^\infty a_n t^n$ is precisely the Maclaurin definition of the target input function $f(t)$, the expression collapses into:
        """)
        st.latex(r"""
        \mathcal{T}\{f\}(s) = \int_0^\infty e^{-st}f(t)g(t) \, dt 
        """)
        st.markdown(r"""
        This completes the rigorous formal proof of the Inverse-Kernel Duality.
        """)
        st.latex(r"""
        \mathcal{T}\{f\}(s) := \sum_{n=0}^\infty a_n (-D_s)^n (G(s)) = \int_0^\infty e^{-st} f(t) g(t) \, dt 
        """)
        st.markdown(r"where $g(t) = \mathcal{L}^{-1}\{G(s)\}(t)$")

    st.markdown(r"""
    **Remark 4.** Theorem 3.1 reveals a two-level conceptual hierarchy in operator geometry. The primary level operates strictly in the $s$-domain via continuous derivative structures of $G(s)$, while the secondary level manifests in the $t$-domain as an integral weighted by the inverse transform of that same kernel.
    """)

    st.subheader("Example 9.2")

    st.markdown(r"""
    Let
    """)
    st.latex(r"""
    G(s) = \frac{s}{s^2 + b^2}, \quad g(t) = \mathcal{T}^{-1}\{G\}(t) = \cos(bt),
    """)
    st.markdown(r"Then")
    st.latex(r"""
    \sum_{n=0}^\infty (-1)^n a_n D^n \left( \frac{s}{s^2 + b^2} \right) = \int_0^\infty f(t) e^{-st} \cos(bt) \, dt
    """)

    st.subheader("Example 9.3")

    st.markdown(r"""
    Let
    """)
    st.latex(r"""
    G(s) = \frac{b}{s^2 + b^2}, \quad g(t) = \mathcal{T}^{-1}\{G\}(t) = \sin(bt),
    """)
    st.markdown(r"Then")
    st.latex(r"""
    \sum_{n=0}^\infty (-1)^n a_n D^n \left( \frac{b}{s^2 + b^2} \right) = \int_0^\infty f(t) e^{-st} \sin(bt) \, dt
    """)
    st.markdown(r"confirming perfect equivalence between the planted-operator form and its integral representation.")

    # ============================================================
    # SECTION 9.2: Using the Inverse-Kernel Duality and proving
    # ============================================================
    st.header("9.2 Using the Inverse-Kernel Duality and proving the transform results")

    st.markdown(r"""
    The following classical results are obtained:
    """)
    st.latex(r"""
    \mathcal{L}\{t^n \sin(bt)\}(s) = \frac{n!}{r^{n+1}} \sin((n+1)\theta).
    """)
    st.latex(r"""
    \mathcal{L}\{t^n \cos(bt)\}(s) = \frac{n!}{r^{n+1}} \cos((n+1)\theta).
    """)
    st.markdown(r"and Classical Mellin.")
    st.latex(r"""
    \int_0^\infty t^{\rho-1} \sin t \, dt = \Gamma(\rho) \sin\left(\frac{\pi \rho}{2}\right), \quad 0 < \Re(\rho) < 1.
    """)
    st.latex(r"""
    \int_0^\infty t^{\rho-1} \cos t \, dt = \Gamma(\rho) \cos\left(\frac{\pi \rho}{2}\right), \quad 0 < \Re(\rho) < 1.
    """)
    st.markdown(r"where")
    st.latex(r"""
    r = \sqrt{s^2 + b^2}, \quad \theta = \arctan\left(\frac{b}{s}\right).
    """)

    # PROOF for sin case
    with st.expander("Show Proof for sin case"):
        st.markdown(r"""
        **Proof.** from the formula
        """)
        st.latex(r"""
        T\{f(t)\}(s) = \sum_{n=0}^\infty (-1)^n a_n D^n \left( \frac{1}{s^2 + 1} \right) = \int_0^\infty e^{-st} f(t) \sin t \, dt.
        """)
        st.markdown(r"""
        We now exploit the algebraic decomposition
        """)
        st.latex(r"""
        \frac{1}{s^2 + 1} = \frac{1}{2i} \left( \frac{1}{s - i} - \frac{1}{s + i} \right),
        """)
        st.markdown(r"so that")
        st.latex(r"""
        T\{f(t)\}(s) = \sum_{n=0}^\infty (-1)^n a_n D^n \left( \frac{1}{s^2 + 1} \right)
        """)
        st.latex(r"""
        = \sum_{n=0}^\infty (-1)^n a_n D^n \left( \frac{1}{2i} \left[ \frac{1}{s - i} - \frac{1}{s + i} \right] \right)
        """)
        st.latex(r"""
        = \frac{1}{2i} \sum_{n=0}^\infty (-1)^n a_n D^n \left( \frac{1}{s - i} \right) - \frac{1}{2i} \sum_{n=0}^\infty (-1)^n a_n D^n \left( \frac{1}{s + i} \right).
        """)
        st.markdown(r"""
        We also use the standard identity
        """)
        st.latex(r"""
        D^n \left( \frac{1}{s - a} \right) = (-1)^n n! (s - a)^{-(n+1)}, \quad n \geq 0,
        """)
        st.markdown(r"valid for any complex constant $a$.")
        st.markdown(r"""
        For convenience, we introduce the polar representation
        """)
        st.latex(r"""
        s \pm i = re^{\pm i\theta}, \quad r = \sqrt{s^2 + 1}, \quad \theta = \arctan \left( \frac{1}{s} \right).
        """)
        st.markdown(r"""
        Applying $D^n$ to the above decomposition gives
        """)
        st.latex(r"""
        D^n \left( \frac{1}{s^2 + 1} \right) = \frac{(-1)^n n!}{2i} \left( (s - i)^{-(n+1)} - (s + i)^{-(n+1)} \right)
        """)
        st.latex(r"""
        = \frac{(-1)^n n!}{2i r^{n+1}} \left( e^{-i(n+1)\theta} - e^{i(n+1)\theta} \right)
        """)
        st.latex(r"""
        = (-1)^n n! \frac{\sin((n+1)\theta)}{r^{n+1}}.
        """)
        st.markdown(r"""
        **Step 2. Polar differential structure.** From the derivations established in Section 2, the $n$th derivative of this kernel admits the polar form
        """)
        st.latex(r"""
        D^n G(s) = (-1)^n n! \frac{\sin((n+1)\theta)}{r^{n+1}}, \quad r = \sqrt{s^2 + 1}, \quad \theta = \arctan \left( \frac{1}{s} \right).
        """)
        st.markdown(r"""
        **Step 3. Operator–planted series.** For an analytic function
        """)
        st.latex(r"f(t) = \sum_{n=0}^{\infty} a_n t^n,")
        st.markdown(r"the planted form of the transform is")
        st.latex(r"""
        T\{f\}(s) = \sum_{n=0}^\infty (-1)^n a_n D^n G(s) = \sum_{n=0}^\infty a_n n! \frac{\sin((n+1)\theta)}{r^{n+1}}.
        """)
        st.markdown(r"""
        **Step 4** when $f(t) = t^n$ the series becomes $(-1)^n D^n (G(s))$
        """)
        st.latex(r"""
        D^n G(s) = (-1)^n n! \frac{\sin((n+1)\theta)}{r^{n+1}}, \quad r = \sqrt{s^2 + 1}, \quad \theta = \arctan \left( \frac{1}{s} \right).
        """)
        st.latex(r"""
        (-1)^n n! \frac{\sin((n+1)\theta)}{r^{n+1}} = \int_0^\infty e^{-st} t^n \sin t \, dt.
        """)
        st.latex(r"""
        \frac{n! \sin((n+1)\theta)}{r^{n+1}} = \int_0^\infty e^{-st} t^n \sin t \, dt.
        """)
        st.latex(r"""
        = \mathcal{L}\{t^n \sin(bt)\}(s)
        """)
        st.markdown(r"""
        **Step 5. Taking the limit $s \to 0^+$.** On the operator side,
        """)
        st.latex(r"""
        r = \sqrt{s^2 + 1} \to 1, \quad \theta = \arctan\left(\frac{1}{s}\right) \to \frac{\pi}{2}.
        """)
        st.markdown(r"Thus,")
        st.latex(r"""
        \mathcal{T}\{f\}(s) = \sum_{n=0}^\infty a_n n! \sin\left((n+1)\frac{\pi}{2}\right)
        """)
        st.latex(r"""
        \mathcal{T}\{f\}(s) = \sum_{n=0}^\infty a_n n! \cos\left(\frac{n\pi}{2}\right)
        """)
        st.markdown(r"""
        We start from the structural identity
        """)
        st.latex(r"""
        \sum_{n=0}^\infty a_n n! \cos\left(\frac{n\pi}{2}\right) = \int_0^\infty f(t) \sin t \, dt,
        """)
        st.markdown(r"valid for any analytic function")
        st.latex(r"f(t) = \sum_{n=0}^\infty a_n t^n")
        st.markdown(r"Let")
        st.latex(r"f(x) = t^{p-1}.")
        st.markdown(r"Then")
        st.latex(r"""
        \int_0^\infty t^{p-1} \sin t \, dt = (p-1)! \cos\left(\frac{\pi p}{2} - \frac{\pi}{2}\right).
        """)
        st.markdown(r"Since")
        st.latex(r"""
        \cos\left(\frac{\pi p}{2} - \frac{\pi}{2}\right) = \Gamma(p) \sin\left(\frac{\pi p}{2}\right),
        """)
        st.markdown(r"we obtain")
        st.latex(r"""
        \int_0^\infty t^{p-1} \sin t \, dt = \Gamma(p) \sin\left(\frac{\pi p}{2}\right), \quad 0 < \Re(p) < 1.
        """)

    # PROOF for cos case
    with st.expander("Show Proof for cos case"):
        st.markdown(r"""
        **Proof. 2**
        """)
        st.latex(r"""
        T\{f(t)\}(s) = \sum_{n=0}^\infty (-1)^n a_n D^n\left(\frac{s}{s^2 + 1}\right) = \int_0^\infty e^{-st} f(t) \cos t \, dt.
        """)
        st.markdown(r"""
        **Step 1. Derivative Structure of the Rational Kernel**
        """)
        st.markdown(r"""
        We recall the decomposition
        """)
        st.latex(r"""
        \frac{s}{s^2+1} = \frac{1}{2} \left( \frac{1}{s-i} + \frac{1}{s+i} \right).
        """)
        st.markdown(r"""
        We also use the standard identity
        """)
        st.latex(r"""
        D^n \left( \frac{1}{s-a} \right) = (-1)^n n! (s-a)^{-(n+1)}, \quad n \geq 0,
        """)
        st.markdown(r"valid for any complex constant $a$.")
        st.markdown(r"""
        For convenience, we introduce the polar representation
        """)
        st.latex(r"""
        s \pm i = re^{\pm i\theta}, \quad r = \sqrt{s^2+1}, \quad \theta = \arctan \left( \frac{1}{s} \right).
        """)
        st.markdown(r"""
        Derivative of $\frac{s}{s^2+1}$
        """)
        st.latex(r"""
        D^n \left( \frac{s}{s^2+1} \right) = \frac{(-1)^n n!}{2} \left( (s-i)^{-(n+1)} + (s+i)^{-(n+1)} \right)
        """)
        st.latex(r"""
        = \frac{(-1)^n n!}{2r^{n+1}} \left( e^{-i(n+1)\theta} + e^{i(n+1)\theta} \right)
        """)
        st.latex(r"""
        = (-1)^n n! \frac{\cos((n+1)\theta)}{r^{n+1}}.
        """)
        st.markdown(r"""
        **Step 2. Polar differential structure.** From the derivations established in Section 2, $n$th derivative of this kernel admits the polar form
        """)
        st.latex(r"""
        D^n G(s) = (-1)^n n! \frac{\cos((n+1)\theta)}{r^{n+1}}, \quad r = \sqrt{s^2+1}, \quad \theta = \arctan \left( \frac{1}{s} \right).
        """)
        st.markdown(r"""
        **Step 3. Operator–planted series.** For an analytic function
        """)
        st.latex(r"f(t) = \sum_{n=0}^{\infty} a_n t^n,")
        st.markdown(r"the planted form of the transform is")
        st.latex(r"""
        \mathcal{T}\{f\}(s) = \sum_{n=0}^{\infty} (-1)^n a_n D^n G(s) = \sum_{n=0}^{\infty} a_n n! \frac{\cos((n+1)\theta)}{r^{n+1}}.
        """)
        st.markdown(r"""
        **Step 4** when $f(t) = t^n$ the series becomes $(-1)^n D^n(G(s))$
        """)
        st.latex(r"""
        D^n G(s) = (-1)^n n! \frac{\cos((n+1)\theta)}{r^{n+1}}, \quad r = \sqrt{s^2 + 1}, \quad \theta = \arctan \left( \frac{1}{s} \right).
        """)
        st.latex(r"""
        (-1)^n n! \frac{\cos((n+1)\theta)}{r^{n+1}} = \int_0^\infty e^{-st} t^n \cos t \, dt.
        """)
        st.latex(r"""
        \frac{n! \cos((n+1)\theta)}{r^{n+1}} = \int_0^\infty e^{-st} t^n \cos t \, dt.
        """)
        st.latex(r"""
        = \mathcal{L}\{t^n \cos(bt)\}(s)
        """)
        st.markdown(r"""
        **Step 5. Taking the limit $s \to 0^+$**
        On the operator side,
        """)
        st.latex(r"""
        r = \sqrt{s^2 + 1} \to 1, \quad \theta = \arctan\left(\frac{1}{s}\right) \to \frac{\pi}{2}.
        """)
        st.markdown(r"Thus,")
        st.latex(r"""
        \mathcal{T}\{f\}(t) = \sum_{n=0}^\infty a_n n! \cos\left((n+1)\frac{\pi}{2}\right)
        """)
        st.latex(r"""
        \mathcal{T}\{f\}(s) = -\sum_{n=0}^\infty a_n n! \sin\left(\frac{n\pi}{2}\right)
        """)
        st.markdown(r"""
        We start from the structural identity
        """)
        st.latex(r"""
        -\sum_{n=0}^\infty a_n n! \sin\left(\frac{n\pi}{2}\right) = \int_0^\infty f(t) \cos t \, dt,
        """)
        st.markdown(r"valid for any analytic function")
        st.latex(r"f(t) = \sum_{n=0}^\infty a_n t^n")
        st.markdown(r"Let")
        st.latex(r"f(t) = t^{\rho-1}.")
        st.markdown(r"Then")
        st.latex(r"""
        \int_0^\infty t^{\rho-1} \cos t \, dt = -(\rho-1)! \sin\left(\frac{\pi\rho}{2} - \frac{\pi}{2}\right).
        """)
        st.markdown(r"""
        We now expand using the angle subtraction identity:
        """)
        st.latex(r"""
        \sin\left(\frac{\pi\rho}{2} - \frac{\pi}{2}\right) = \sin\left(\frac{\pi\rho}{2}\right) \cos\left(\frac{\pi}{2}\right) - \cos\left(\frac{\pi\rho}{2}\right) \sin\left(\frac{\pi}{2}\right),
        """)
        st.markdown(r"so that")
        st.latex(r"""
        -(\rho-1)! \sin\left(\frac{\pi\rho}{2} - \frac{\pi}{2}\right) = -(\rho-1)! \left(0 - \cos\left(\frac{\pi\rho}{2}\right)\right) = (\rho-1)! \cos\left(\frac{\pi\rho}{2}\right).
        """)
        st.markdown(r"Therefore,")
        st.latex(r"""
        \int_0^\infty t^{\rho-1} \cos t \, dt = \Gamma(\rho) \cos\left(\frac{\pi\rho}{2}\right), \quad 0 < \Re(\rho) < 1.
        """)

    # ============================================================
    # SECTION 9.3 to 9.10 (will be added after receiving remaining pages)
    # ============================================================
   

if __name__ == "__main__":
    render_unified_framework_section()
