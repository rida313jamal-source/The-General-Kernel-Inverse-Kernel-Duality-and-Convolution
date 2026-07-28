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
    # SECTION 9.4: Kernel Multiplication and Boundary Contribution
    # ============================================================
    st.header("9.4 Kernel Multiplication and Boundary Contribution")

    st.markdown(r"""
    Returning to the general formula (Inverse-Kernel Duality)
    """)
    st.latex(r"""
    T\{f\}(s) := \sum_{n=0}^{\infty} a_n(-D_s)^n(G(s)) = \int_0^{\infty} e^{-st}f(t)g(t)dt
    """)
    st.markdown(r"where $g(t) = \mathcal{L}^{-1}\{G(s)\}(t)$")

    st.markdown(r"""
    Having established the foundational mapping, we now analyze how algebraic operations on the generated kernel $G(s)$ inject specific calculus operators into the spatial domain. We begin with the multiplication operator, which systematically injects differentiation into the inverse kernel.
    """)

    st.subheader("Lemma 9.4 (Kernel Multiplication and Boundary Contribution)")

    st.markdown(r"""
    Let
    """)
    st.latex(r"""
    G(s) = \int_0^{\infty} e^{-st}g(t)dt
    """)
    st.markdown(r"""
    be an inverse-kernel representation, where $g$ is locally absolutely continuous on $[0, \infty)$ and of sufficient decay at infinity. Then multiplication of the kernel by $s$ satisfies:
    """)
    st.latex(r"""
    sG(s) = g(0) + \int_0^{\infty} e^{-st}g'(t)dt,
    """)
    st.markdown(r"and hence, in the sense of inverse kernels,")
    st.latex(r"""
    T^{-1}\{sG(s)\}(t) = g'(t) + g(0)\delta(t).
    """)
    st.markdown(r"""
    In particular, the boundary contribution depends exclusively on the value of the original inverse kernel $g(t)$ at the origin, and not on the values of its derivatives. At $g(0) = 0$:
    """)
    st.latex(r"""
    sG(s) = \int_0^{\infty} e^{-st}g'(t)dt,
    """)
    st.markdown(r"for second derivative also:")
    st.latex(r"""
    s^2G(s) = \int_0^{\infty} e^{-st}g''(t)dt,
    """)
    st.markdown(r"for $n$-th:")
    st.latex(r"""
    s^nG(s) = \int_0^{\infty} e^{-st}g^{(n)}(t)dt,
    """)
    st.markdown(r"that implies to:")
    st.latex(r"""
    T^{-1}\{s^nG(s)\}(t) = g^{(n)}(t).
    """)

    st.markdown(r"""
    **Remark 5.** The boundary term $g(0)\delta(t)$ is determined solely by the inverse kernel $g$ associated with the original kernel $G(s)$. If $sG(s)$ is rewritten in closed form and admits a different inverse kernel $\tilde{g}(t)$, the value $\tilde{g}(0)$ does not generate a new boundary contribution. Boundary terms are evaluated only once, at the level of the original kernel before multiplication by $s$.

    **Conclusion.** Multiplication by $s$ injects differentiation into the inverse kernel, while boundary contributions arise if and only if the original inverse kernel is nonzero at the origin. This mechanism is intrinsic to the inverse-kernel representation and is independent of any subsequent rewriting of the kernel.
    """)

    # ============================================================
    # SECTION 9.5: Kernel Division and Integral Injection
    # ============================================================
    st.header("9.5 Kernel Division and Integral Injection")

    st.markdown(r"""
    We now turn to the inverse operation. While multiplication by $s$ acts as a differential injector carrying boundary baggage, division by $s$ acts as a pure integration injector that is entirely boundary-safe.
    """)

    st.subheader("Lemma 9.5 (Kernel Division and Integral Injection)")

    st.markdown(r"""
    Let
    """)
    st.latex(r"""
    G(s) = \int_0^\infty e^{-st} g(t) \, dt
    """)
    st.markdown(r"""
    be an inverse-kernel representation, where $g \in L_{loc}^1([0, \infty))$ and the integrals below are justified (e.g., by Tonelli/Fubini under absolute integrability). Define:
    """)
    st.latex(r"""
    H(s) := \frac{G(s)}{s}, \quad \Re(s) > 0.
    """)
    st.markdown(r"""
    Then $H$ admits the inverse-kernel representation:
    """)
    st.latex(r"""
    H(s) = \int_0^\infty e^{-st} h(t) \, dt, \quad \text{where } h(t) = \int_0^t g(u) \, du.
    """)
    st.markdown(r"""
    Equivalently, in the sense of inverse kernels,
    """)
    st.latex(r"""
    \mathcal{T}^{-1} \left\{ \frac{G(s)}{s} \right\} (x) = \int_0^x g(u) \, du.
    """)
    st.markdown(r"""
    More generally, for any integer $k \geq 1$,
    """)
    st.latex(r"""
    \mathcal{T}^{-1} \left\{ \frac{G(s)}{s^k} \right\} (t) = \int_0^t \int_0^{u_1} \cdots \int_0^{u_{k-1}} g(u_k) \, du_k \cdots du_2 \, du_1,
    """)
    st.markdown(r"""
    i.e., division by $s^k$ injects $k$-fold integration into the inverse kernel.
    """)

    with st.expander("Show Proof of Lemma 9.5"):
        st.markdown(r"""
        **Proof.** We use the elementary identity (valid for $\Re(s) > 0, u \geq 0$):
        """)
        st.latex(r"""
        \frac{e^{-su}}{s} = \int_0^\infty e^{-st} \, dt.
        """)
        st.markdown(r"""
        Starting from $H(s) = G(s)/s$ and the representation of $G$, we write:
        """)
        st.latex(r"""
        \frac{G(s)}{s} = \int_0^\infty e^{-su} g(u) \, du = \int_0^\infty \left( \int_u^\infty e^{-st} \, dt \right) g(u) \, du.
        """)
        st.markdown(r"""
        Assuming absolute integrability so that Tonelli/Fubini applies, we interchange the order of integration:
        """)
        st.latex(r"""
        \frac{G(s)}{s} = \int_0^\infty e^{-st} \left( \int_0^t g(u) \, du \right) dt.
        """)
        st.markdown(r"""
        Hence $H(s) = \int_0^\infty e^{-st} h(t) \, dt$ with $h(t) = \int_0^t g(u) \, du$, proving the $k = 1$ case.

        For $k \geq 2$, iterate the same argument (or apply the $k = 1$ case repeatedly to $G/s^{k-1}$), which yields the stated $k$-fold integral formula.
        """)

    st.markdown(r"""
    **Remark 6.** Unlike multiplication by $s$, division by $s$ produces no boundary term: there is no integration by parts, hence no evaluation at $t = 0$ or $t = \infty$. Therefore, the integral-injection law is boundary-safe and depends only on the integrability needed to justify the interchange of integrals.
    """)

    # ============================================================
    # SECTION 9.6: The Cauchy Reduction Principle
    # ============================================================
    st.header("9.6 The Cauchy Reduction Principle and Fractional Integral Injection")

    st.markdown(r"""
    The $k$-fold nested integral obtained from the division operator $s^k$ poses a practical challenge for analytical evaluation due to its multi-layered complexity. To collapse this multi-dimensional spatial structure into a single-variable representation, we invoke the classical Cauchy Formula for Repeated Integration.
    """)

    st.subheader("Theorem 9.6 (Cauchy Reduction of the Operator Kernel)")

    st.markdown(r"""
    Let $k \in \mathbb{N}$ and let $g(t)$ be a locally integrable function on $[0, \infty)$. The $k$-fold repeated integral mapping of the inverse kernel can be rigorously reduced to a single continuous integral weighted by a polynomial kernel:
    """)
    st.latex(r"""
    \int_0^t \int_0^{u_1} \cdots \int_0^{u_{k-1}} g(u_k) du_k \cdots du_2 du_1 = \frac{1}{(k-1)!} \int_0^t (t-\tau)^{k-1} g(\tau) d\tau
    """)
    st.markdown(r"""
    Recognizing that $(m-1)! \cdot m = m!$, the expression simplifies smoothly to:
    """)
    st.latex(r"""
    I^{m+1}[g](t) = \frac{1}{m!} \int_0^t (t-\tau)^m g(\tau) d\tau
    """)
    st.markdown(r"""
    This confirms that the relation holds true for $k = m+1$, completing the rigorous inductive proof.
    """)

    # ============================================================
    # SECTION 9.7: Generalization to Continuous Fractional Calculus Domains
    # ============================================================
    st.header("9.7 Generalization to Continuous Fractional Calculus Domains")

    st.markdown(r"""
    The structural elegance of the Cauchy reduction is that the factorial term $(k-1)!$ can be extended analytically to non-integer domains via the Euler Gamma function $\Gamma(\cdot)$. This allows us to transition from discrete integer division to continuous fractional operators.
    """)

    st.subheader("Definition 9.7 (Fractional Integral Injection Operator)")

    st.markdown(r"""
    Let $\alpha \in \mathbb{R}^+$ be an arbitrary positive fractional rank. The division of a generalized kernel $G(s)$ by the continuous fractional power $s^\alpha$ induces a continuous convolution weight into the inverse-kernel spatial domain:
    """)
    st.latex(r"""
    \mathcal{T}\{f\}(s) := \int_0^\infty a_n(-D_s)^n \frac{G(s)}{s^\alpha} = \int_0^\infty e^{-st} f(t) \cdot \frac{1}{\Gamma(\alpha)} \int_0^t (t-\tau)^{\alpha-1} g(\tau) d\tau dt
    """)
    st.markdown(r"where $\Gamma(\alpha) = \int_0^\infty t^{\alpha-1} e^{-t} dt$.")
    st.latex(r"""
    \mathcal{T}\{f\}(s) := \sum_{n=0}^\infty a_n(-D_s)^n \frac{G(s)}{s^\alpha} = \int_0^\infty e^{-st} f(t) \cdot \frac{1}{\Gamma(\alpha)} \int_0^t (t-\tau)^{\alpha-1} g(\tau) d\tau dt
    """)
    st.markdown(r"""
    This operator explicitly represents the generalized Riemann-Liouville fractional integral of the spatial seed function $g(t)$. If the framework is anchored to the foundational baseline from the first monograph where $G(s) = 1/s$ (and consequently $g(t) = 1$), the expression yields:
    """)
    st.latex(r"""
    \mathcal{T}^{-1}\left\{\frac{1}{s^{\alpha+1}}\right\}(t) = \frac{1}{\Gamma(\alpha)} \int_0^t (t-\tau)^{\alpha-1} g(\tau) d\tau = \frac{t^\alpha}{\Gamma(\alpha+1)}
    """)
    st.markdown(r"""
    This perfectly aligns with classical fractional calculus definitions, demonstrating that our generalized core embeds standard fractional integration as a simple boundary restriction.
    """)

    # ============================================================
    # SECTION 9.8: The General Rational Operator and Convolution Domain Integration
    # ============================================================
    st.header("9.8 The General Rational Operator and Convolution Domain Integration")

    st.markdown(r"""
    The architectural expansion of the division law requires moving beyond a simple monomial denominator $s^k$ toward an arbitrary polynomial operator $P(s)$ acting in the transform domain. This structural modification establishes how rational operator fractions blend different kernel properties through spatial convolution.
    """)

    st.subheader("Theorem 9.8 (The Generalized Convolution Kernel Identity)")

    st.markdown(r"""
    Let $G(s) = \int_0^\infty e^{-st}g(t) dt$ be a continuous inverse-kernel representation. Let $P(s)$ be an algebraic polynomial in the transform parameter $s$ such that its reciprocal admits a well-defined spatial weight function $h(t) = \mathcal{L}^{-1} \left\{ \frac{1}{P(s)} \right\} (t)$. Define the compound rational transform operator $W(s)$ as:
    """)
    st.latex(r"""
    W(s) := \frac{G(s)}{P(s)}
    """)
    st.markdown(r"""
    Then the structural inversion of $W(s)$ maps directly onto a closed spatial convolution integral where the properties of $g(t)$ and $h(t)$ are dynamically interrelated:
    """)
    st.latex(r"""
    \mathcal{T}^{-1} \left\{ \frac{G(s)}{P(s)} \right\} (t) = \int_0^t h(t - \tau)g(\tau) \, d\tau
    """)

    with st.expander("Show Proof of Theorem 9.8"):
        st.markdown(r"""
        **Proof.** By writing the rational operator as a direct multiplication of two separate transform architectures, we isolate the components in the transform domain:
        """)
        st.latex(r"""
        \frac{G(s)}{P(s)} = \left( \frac{1}{P(s)} \right) \cdot G(s)
        """)
        st.markdown(r"""
        Substituting the explicit integral representations for both components based on their independent spatial domains, we introduce the dummy variables $\tau$ and $u$:
        """)
        st.latex(r"""
        \frac{G(s)}{P(s)} = \left( \int_0^\infty e^{-su}h(u) \, du \right) \cdot \left( \int_0^\infty e^{-s\tau}g(\tau) \, d\tau \right)
        """)
        st.markdown(r"""
        Assuming absolute integrability conditions are satisfied, we apply the Fubini-Tonelli theorem to unify the product into a joint double integral over the quarter-plane region $[0, \infty) \times [0, \infty)$:
        """)
        st.latex(r"""
        \frac{G(s)}{P(s)} = \int_0^\infty \int_0^\infty e^{-s(u+\tau)}h(u)g(\tau) \, du \, d\tau
        """)
        st.markdown(r"""
        To align this structure with a single standard transform format, we perform a linear transformation of variables to isolate the exponential decay parameter. Let $t = u + \tau$, which implies $u = t - \tau$. The differential maps as $du = dt$. The integration boundary variable $t$ spans from $\tau$ to $\infty$:
        """)
        st.latex(r"""
        \frac{G(s)}{P(s)} = \int_0^\infty \left( \int_t^\infty e^{-st}h(t - \tau)g(\tau) \, d\tau \right) \, dt
        """)
        st.markdown(r"""
        Reversing the order of integration across the triangular boundary domain $\Omega = \{(t, \tau) : 0 \leq \tau \leq t < \infty\}$, the outer integral becomes bounded by the absolute spatial continuum while the inner integral captures the shifting parameter:
        """)
        st.latex(r"""
        \frac{G(s)}{P(s)} = \int_0^\infty e^{-st} \left( \int_0^t h(t - \tau)g(\tau) \, d\tau \right) \, dt
        """)
        st.markdown(r"""
        By inspecting the internal nested integral, we recognize it as the exact convolution definition. Applying the inversion mapping operator $\mathcal{T}^{-1}$ proves the core assertion:
        """)
        st.latex(r"""
        \mathcal{T}^{-1} \left\{ \frac{G(s)}{P(s)} \right\} (t) = \int_0^t h(t - \tau)g(\tau) \, d\tau
        """)
        st.markdown(r"This completes the formal proof of the generalized convolution kernel framework.")

    st.subheader("Corollary 9.9 (Compound Rational Operator Law)")

    st.markdown(r"""
    Let $n \in \mathbb{N}_0$ and let $P(s)$ be a transform domain polynomial operator generating the inverse mapping response $h(t)$. The total inversion of a generated kernel divided by both polynomial layers resolves into a nested integral structure:
    """)
    st.latex(r"""
    T^{-1} \left\{ \frac{G(s)}{s^n P(s)} \right\} (t) = \frac{1}{(n-1)!} \int_0^t (t-\tau)^{n-1} \left( \int_0^{\tau} h(\tau - z)g(z) \, dz \right) \, d\tau
    """)
    st.markdown(r"""
    Alternatively, invoking the associativity and commutativity properties of spatial convolution, the operational structure can be consolidated into a single directional integral:
    """)
    st.latex(r"""
    T^{-1} \left\{ \frac{G(s)}{s^n P(s)} \right\} (t) = \int_0^t K_{n,P}(t-\tau) g(\tau) d\tau
    """)
    st.markdown(r"""
    where $K_{n,P}(t) = \mathcal{L}^{-1} \left\{ \frac{1}{s^n P(s)} \right\} (t)$ represents the total compound baseline response function.
    """)

    st.latex(r"""
    T\{f\}(s) := \sum_{n=0}^{\infty} a_n(-D_s)^n \frac{G(s)}{P(s)} = \int_0^{\infty} e^{-st} f(t) \int_0^t h(t-\tau) g(\tau) d\tau,
    """)

    

    

    

if __name__ == "__main__":
    render_unified_framework_section() 


